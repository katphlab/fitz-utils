## Introduction
Add extra functions for use with pymupdf module

## Installation
Only this step is required if you want to install `fitz_utils` package in your project.

1. Ensure wheel and setuptools packages are installed in the environment
```
pip install wheel==0.38.4 setuptools==65.5.1
```
2. Create wheel of the package
```
python setup.py bdist_wheel
```
3. Install the package
```
pip install dist/fitz_utils-0.0.11-py3-none-any.whl
```
4. Install the package with poetry (If you're using poetry) - OPTIONAL <br/>
Copy the `dist/fitz_utils-0.0.11-py3-none-any.whl` into your project folder such as `your_project/packages/fitz-utils/fitz_utils-0.0.11-py3-none-any.whl`
```
poetry add packages/fitz-utils/fitz_utils-0.0.11-py3-none-any.whl
```

## How to Export the Environment
1. Export the requirements.txt with pip
```
pip freeze > requirements/requirements.txt
```
2. Export the environment.yaml with conda
```
conda env export --no-builds > requirements/environment.yaml
```

## How to Import the Environment
If you're using the conda, please use the second way.

1. Install the requirements.txt with pip
```
pip install -r requirements/requirements.txt
```
2. Create the conda environment with environment.yaml
```
conda env create -f requirements/environment.yaml
```

## Install the [pre-commit hook](https://pre-commit.com/)
To meet with the coding guidelines and standards, please run this command after
installing the requirements.
```
pre-commit install
```
