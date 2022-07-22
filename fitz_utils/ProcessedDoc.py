from pathlib import Path
import fitz

from .ProcessedPage import ProcessedPage


class ProcessedDoc:
    """Class to provide extra methods to pymupdf doc class"""

    def __init__(self, fname: Path) -> None:
        self.doc = fitz.open(str(fname))
        pass

    def __getitem__(self, key):
        return ProcessedPage(self.doc[key])
