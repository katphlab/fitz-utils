## **[0.0.16] 06-01-2024**

- Update PyMuPDF version for compatibility with PaddleOCR
- ProcessedDoc
  - **crop_pdf_bytes** -> Crop pages of a pdf as another pdf and return bytes

## **[0.0.15] 20-10-2023**

- ProcessedDoc
  - **Fix circular imports**

## **[0.0.14] 06-07-2023**

### **[Added]**

- ProcessedPage
  - **get_word_df_within_bbox** -> Get all the words within a bbox
  - **get_span_df_within_bbox** -> Get all the spans within a bbox
  - **get_line_df_within_bbox** -> Get all the lines within a bbox

## **[0.0.13] 30-05-2023**

### **[Added]**

- ProcessedPage
  - **is_text_horizontal** -> Check if the text orientation of the page is horizontal

## **[0.0.12] 16-05-2023**

### **[Modified]**

- ProcessedPage
  - **is_digital** -> Added the rect parameter to check if the ROI is digital

## **[0.0.11] 15-05-2023**

### **[Modified]**

- ProcessedPage
  - **get_block_df** -> Added fixed_text column with the ftfy library
  - **get_line_df** -> Added fixed_text column with the ftfy library
  - **get_span_df** -> Added fixed_text column with the ftfy library
  - **get_word_df** -> Added fixed_text column with the ftfy library

## **[0.0.10] 12-05-2023**

### **[Added]**

- ProcessedPage
  - **get_line_df** -> Get the text of the page line by line and return it as the dataframe

## **[0.0.9] 11-05-2023**

### **[Added]**

- ProcessedPage
  - **is_digital** -> Check whether the page is digital or scan

## **[0.0.8] 08-02-2023**

### **[Added]**

- fitz_utils
  - Update **init** to add classes.

## **[0.0.7] 22-12-2022**

### **[Modified]**

- ProcessedDoc
  - Updated to support reading from the bytes stream.
  - Added the file extension ".md" to the CHANGELOG as CHANGELOG.md.

## **[0.0.6] 15-11-2022**

### **[Modified]**

- ProcessedPage
  - Added the dpi support as an alternative to the fitz.Matrix
  - Added the pre-commit hook to control the coding standards
  - Updated the readme to provide instructions to requirements and pre-commit

## **[0.0.5] 26-09-2022**

### **[Modified]**

- ProcessedDoc
  - Added the \_\_len\_\_ magic method to get the document length

## **[0.0.4] 01-08-2022**

### **[Added]**

- Unit Test for get_unformatted_opencv_img
- Add tests dependency in setup.py

### **[Modified]**

- ProcessedPage
  - **get_unformatted_opencv_img** -> Creates an image after placing text from page on an empty page

## **[0.0.3] 26-07-2022**

### **[Modified]**

- ProcessedPage
  - **get_opencv_img** -> Takes scale argument to scale the page pixmap

## **[0.0.2] 25-07-2022**

### **[Added]**

- ProcessedPage
  - **get_opencv_img** -> Returns opencv image of page

## **[0.0.1] 22-07-2022**

- First Release

### **[Added]**

- ProcessedPage
  - Get Fonts Flag
  - Get Block dataframe
  - Get Span dataframe
  - Get Word dataframe
- ProcessedDoc
  - Add indexing
