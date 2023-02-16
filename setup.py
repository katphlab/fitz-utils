from distutils.core import setup

package = "fitz-utils"
description = "Add extra functions for use with pymupdf module"
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=package,
    version="0.0.8",
    install_requires=["numpy>", "pandas", "pymupdf"],
    tests_require=["pytest", "opencv-python"],
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["fitz_utils"],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.9",
)
