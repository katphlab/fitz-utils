import fitz
import numpy as np
import pandas as pd
import ftfy


class ProcessedPage:
    """Class to provide extra methods to pymupdf page class"""

    def __init__(self, page: fitz.Page) -> None:
        self.page = page

    def get_font_flags(self, flags: int) -> list:
        """Make font flags human readable.

        Args:
            flags (int): flag integer from pymupdf

        Returns:
            list: comma separated font flags
        """
        font_flags = []
        if flags & 2**0:
            font_flags.append("superscript")
        if flags & 2**1:
            font_flags.append("italic")
        if flags & 2**2:
            font_flags.append("serifed")
        else:
            font_flags.append("sans")
        if flags & 2**3:
            font_flags.append("monospaced")
        else:
            font_flags.append("proportional")
        if flags & 2**4:
            font_flags.append("bold")
        return font_flags

    def get_block_df(self) -> pd.DataFrame:
        """Generate blocks dataframe from text of page

        Returns:
            pd.DataFrame: Columns - ["x0", "y0", "x1", "y1", "text", "rect"]
        """
        # Block data format: (x0, y0, x1, y1, "lines in the block", block_no, #
        # block_type) #
        blocks: list = self.page.get_text("blocks")
        cols = ["x0", "y0", "x1", "y1", "text", "rect"]

        block_data = []
        for block in blocks:
            # If block type is image, continue #
            if block[-1] == 1:
                continue
            rect = fitz.Rect(block[:4])
            block = list(block[:5]) + [rect]
            block_data.append(block)
        block_df = pd.DataFrame(block_data, columns=cols)
        float_dtypes = block_df.select_dtypes("float64")
        block_df[float_dtypes.columns] = float_dtypes.astype("int")
        return block_df

    def get_span_df(self) -> pd.DataFrame:
        """Generate spans dataframe from page

        Returns:
            pd.DataFrame: Columns - ["x0", "y0", "x1", "y1", "text", "size",
            "flags","color", "font", "block_num", "line_num", "span_num", "rect"]
        """
        blocks = self.page.get_text("dict")["blocks"]
        cols = ["x0", "y0", "x1", "y1", "text", "size", "flags"]
        cols += ["color", "font", "block_num", "line_num", "span_num", "rect"]

        data = []
        for block_num, block in enumerate(blocks):
            if "image" in block.keys():
                continue
            for line_num, line in enumerate(block["lines"]):
                for span_num, span in enumerate(line["spans"]):
                    rect = fitz.Rect(span["bbox"])
                    if rect not in self.page.rect or set(span["text"]) == {" "}:
                        continue

                    span_data = list(span["bbox"])
                    span_data.append(span["text"])
                    span_data.append(span["size"])
                    span_data.append(span["flags"])
                    span_data.append(fitz.sRGB_to_pdf(span["color"]))
                    span_data.append(span["font"])
                    span_data += [block_num, line_num, span_num, rect]
                    data.append(span_data)

        span_df = pd.DataFrame(data=data, columns=cols)
        float_dtypes = span_df.select_dtypes("float64")
        span_df[float_dtypes.columns] = float_dtypes.astype("int")
        return span_df

    def get_word_df(self) -> pd.DataFrame:
        """Generate words dataframe from page

        Returns:
            pd.DataFrame: ["x0", "y0", "x1", "y1", "text", "block_no",
            "line_no", "word_no", "rect"]
        """
        # Word data format (x0, y0, x1, y1, "word", block_no, line_no, word_no) #
        words: list = self.page.get_text("words")
        cols = ["x0", "y0", "x1", "y1", "text", "block_no", "line_no", "word_no"]
        cols += ["rect"]

        word_data = []
        for word in words:
            rect = fitz.Rect(word[:4])
            word = list(word) + [rect]
            word_data.append(word)
        word_df = pd.DataFrame(word_data, columns=cols)
        float_dtypes = word_df.select_dtypes("float64")
        word_df[float_dtypes.columns] = float_dtypes.astype("int")
        return word_df

    def get_opencv_img(
        self, scale: fitz.Matrix = fitz.Matrix(1, 1), dpi: int or None = None
    ) -> np.ndarray:
        """Get opencv image from page

        Args:
            scale (fitz.Matrix): scaling matrix for generating pixmap
            dpi: dots per inch which can be used in place of Matrix

        Returns:
            np.array: Opencv image
        """
        if dpi:
            pix = self.page.get_pixmap(dpi=dpi)
        else:
            pix = self.page.get_pixmap(matrix=scale)

        im = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
        im = np.ascontiguousarray(im[..., [2, 1, 0]])  # rgb to bgr
        return im

    def get_unformatted_opencv_img(self) -> np.ndarray:
        """Generate image of current page by placing text on a blank page to
        remove any fancy formatting from the original page

        Returns:
            np.array: OpenCV image of unformatted page
        """
        df = self.get_word_df()

        temp_doc = fitz.open()
        temp_page = temp_doc.new_page(
            width=self.page.rect.width, height=self.page.rect.height
        )
        df.apply(
            lambda row: temp_page.insert_text(
                (row.x0, row.y1),
                row["text"],
                fontsize=8,
            ),
            axis=1,
        )
        unformatted_img = ProcessedPage(temp_page).get_opencv_img()
        temp_doc.close()
        return unformatted_img

    def is_digital(self) -> bool:
        """Check the page is scan or digital

        Returns:
            bool: True if Digital. False if Scan.
        """
        # Get the list of raw text
        extracted_texts = self.page.get_text().split()

        # Check how many words are likely mojibake
        mojibakes = [
            ftfy.badness.is_bad(extracted_text) for extracted_text in extracted_texts
        ]

        # Get the mojibake and non_mojibake word counts
        total_count = len(extracted_texts)
        mojibakes_count = sum(mojibakes)
        non_mojibackes_count = total_count - mojibakes_count

        # If there is some raw texts in list and majority is non_mojibakes
        if total_count > 0 and mojibakes_count < non_mojibackes_count:
            return True

        return False
