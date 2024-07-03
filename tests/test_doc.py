import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

from fitz_utils import ProcessedDoc, ProcessedPage  # noqa: E402

sample_file = root_dir / "tests" / "files" / "sample.pdf"


def test_open_doc_by_name() -> None:
    doc = ProcessedDoc(fname=sample_file)
    assert isinstance(doc, ProcessedDoc)
    assert len(doc) == 1
    assert isinstance(doc[0], ProcessedPage)


def test_open_doc_by_bytes() -> None:
    with open(sample_file, "rb") as f:
        doc = ProcessedDoc(stream=f.read())
    assert isinstance(doc, ProcessedDoc)
    assert len(doc) == 1
    assert isinstance(doc[0], ProcessedPage)


def test_crop_pdf_bytes() -> None:
    doc = ProcessedDoc(fname=sample_file)
    cropped_doc = doc.crop_pdf_bytes(0, 0)
    assert isinstance(cropped_doc, bytes)
    assert len(cropped_doc) > 0
    assert cropped_doc != doc.write()
