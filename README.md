# OCR Project

## Overview

This project uses OCR to read text from images. It extracts text from `.png` files and outputs the text to corresponding `.txt` files.

## Usage

1. Place your `.png` image files in the `images/` directory.
2. Run the script:
   ```bash
   python main.py
   ```
3. The extracted text will be saved in the `output/` directory.

## Setup

1. **Create and activate a Conda virtual environment:**

   ```bash
   conda create --name ocr_project
   conda activate ocr_project
   ```

2. **Install the required libraries:**

   ```bash
   conda install pillow
   conda install pytesseract
   ```

3. **Install Tesseract-OCR:**
   - **Windows:** Download and install from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
   - **macOS:** `brew install tesseract`
   - **Linux:** `sudo apt-get install tesseract-ocr`

## Project Structure

```
ocr_project/
│
├── images/                # Directory to store .png files
│   ├── example.png
│   └── ...
│
├── output/                # Directory to store output text files
│   ├── example.txt
│   └── ...
│
├── main.py                # Main script for OCR processing
│
└── README.md              # Project documentation
```

This project is helpful for extracting text from images quickly and efficiently.
