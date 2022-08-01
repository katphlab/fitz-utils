import cv2
import pytest
from fitz_utils import ProcessedDoc


class TestProcessedPage:
    @pytest.fixture()
    def processedpage(self):
        doc = ProcessedDoc.ProcessedDoc("fitz_utils/tests/docs/test.pdf")
        yield doc[1]

    def test_get_unformatted_opencv_img_1(self, processedpage):
        result = processedpage.get_unformatted_opencv_img()
        test_result = cv2.imread(
            "fitz_utils/tests/docs/test1_get_unformatted_opencv_img.png"
        )
        assert (result == test_result).all()
