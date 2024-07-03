import sys
from pathlib import Path

import numpy as np
import pandas as pd

root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

from fitz_utils import ProcessedDoc, ProcessedPage  # noqa: E402

sample_file = root_dir / "tests" / "files" / "sample.pdf"


def test_init() -> None:
    doc = ProcessedDoc(fname=sample_file)
    assert isinstance(doc, ProcessedDoc)
    assert len(doc) == 1
    assert isinstance(doc[0], ProcessedPage)


def test_inheritence() -> None:
    doc = ProcessedDoc(fname=sample_file)
    page = doc[0]
    assert page.number == 0
    assert page.rect == page._page.rect


def test_methods_success() -> None:
    doc = ProcessedDoc(fname=sample_file)
    page = doc[0]
    assert isinstance(page.get_block_df(), pd.DataFrame)
    assert isinstance(page.get_line_df(), pd.DataFrame)
    assert isinstance(page.get_span_df(), pd.DataFrame)
    assert isinstance(page.get_word_df(), pd.DataFrame)
    assert isinstance(page.get_opencv_img(), np.ndarray)
    assert isinstance(page.get_unformatted_opencv_img(), np.ndarray)
    assert isinstance(page.is_digital(), bool)
    assert isinstance(page.is_text_horizontal(), bool)
    assert isinstance(page.get_word_df_within_bbox(list(page.rect)), pd.DataFrame)
    assert isinstance(page.get_span_df_within_bbox(list(page.rect)), pd.DataFrame)
    assert isinstance(page.get_line_df_within_bbox(list(page.rect)), pd.DataFrame)
