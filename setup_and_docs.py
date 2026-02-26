# setup.py
from setuptools import setup, find_packages

setup(
    name="baselinewalk",
    version="0.1.0",
    packages=find_packages(),
    py_modules=["baselinewalk"],
    install_requires=[
        "pandas>=1.0",
    ],
    entry_points={
        "console_scripts": [
            "baselinewalk=baselinewalk:main",
        ],
    },
    author="Your Name",
    author_email="your@email.com",
    description="Ambient audio segment harmonizer and baseline comparison CLI tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

# MANIFEST.in
include README.md

# README.md
# BaselineWalk

BaselineWalk is a simple command-line tool that harmonizes segmented ambient audio data for downstream comparison and inspection tasks.

## Installation
```bash
pip install .
```

## Usage
```bash
baselinewalk harmonize \
  --input dataset_canonical/canonical_dataset_v1_2025-12-28T05_46_27Z.csv \
  --output dataset_release/canonical_v1/data/canonical_harmonized.csv
```

By default, it runs with preset paths if no arguments are provided.

## Features
- Cleans and standardizes ambient audio segment datasets
- Adds missing fields like duration, confidence, and audio_path
- CLI accessible with a single command

---
Licensed under the MIT License.
