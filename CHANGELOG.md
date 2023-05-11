## **[0.0.9] 11-05-2023**
### **[Added]**
* ProcessedPage
    * **is_digital** -> Check whether the page is digital or scan


## **[0.0.8] 08-02-2023**
### **[Added]**
* fitz_utils
    * Update __init__ to add classes.

## **[0.0.7] 22-12-2022**
### **[Modified]**
* ProcessedDoc
    * Updated to support reading from the bytes stream.
    * Added the file extension ".md" to the CHANGELOG as CHANGELOG.md.

## **[0.0.6] 15-11-2022**
### **[Modified]**
* ProcessedPage
    * Added the dpi support as an alternative to the fitz.Matrix
    * Added the pre-commit hook to control the coding standards
    * Updated the readme to provide instructions to requirements and pre-commit

## **[0.0.5] 26-09-2022**
### **[Modified]**
* ProcessedDoc
    * Added the \_\_len\_\_ magic method to get the document length

## **[0.0.4] 01-08-2022**
### **[Added]**
* Unit Test for get_unformatted_opencv_img
* Add tests dependency in setup.py
### **[Modified]**
* ProcessedPage
    * **get_unformatted_opencv_img** -> Creates an image after placing text from page on an empty page

## **[0.0.3] 26-07-2022**
### **[Modified]**
* ProcessedPage
    * **get_opencv_img** -> Takes scale argument to scale the page pixmap

## **[0.0.2] 25-07-2022**
### **[Added]**
* ProcessedPage
    * **get_opencv_img** -> Returns opencv image of page

## **[0.0.1] 22-07-2022**
* First Release
### **[Added]**
* ProcessedPage
    * Get Fonts Flag
    * Get Block dataframe
    * Get Span dataframe
    * Get Word dataframe
* ProcessedDoc
    * Add indexing
