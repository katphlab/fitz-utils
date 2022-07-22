import fitz
import pandas as pd


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
            pd.pd.DataFrame: ["x0", "y0", "x1", "y1", "text", "block_no",
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
