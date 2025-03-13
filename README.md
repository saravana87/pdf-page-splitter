# PDF Splitter

This repository contains a simple Python script for splitting a PDF into individual pages. It was created as part of a Proof of Concept (POC) for clinical notes processing, but it can be useful for various PDF-related tasks.

## Features

- Splits multi-page PDFs into separate single-page files.
- Uses **PyMuPDF (Fitz)** for efficient PDF processing.
- Handles errors such as missing files.

## Requirements

Ensure you have the following dependencies installed before running the script:

```bash
pip install pymupdf
```

## Usage

1. Place the PDF file you want to split in the project directory.
2. Update the `input_pdf` variable with the path to your PDF.
3. Set the `output_directory` where the split pages will be saved.
4. Run the script:

```bash
python split_pdf.py
```

## Example Code

```python
import os
import fitz  # PyMuPDF

def split_pdf_pages_fitz(pdf_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    try:
        doc = fitz.open(pdf_path)
        for page_num in range(doc.page_count):
            new_doc = fitz.open()
            new_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)
            output_pdf_path = os.path.join(output_dir, f"page_{page_num + 1}.pdf")
            new_doc.save(output_pdf_path)
            new_doc.close()
        doc.close()
        print(f"Pages successfully split and saved in {output_dir}")
    except FileNotFoundError:
        print(f"Error: PDF file not found at {pdf_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
input_pdf = "./splitpdf/CLINICAL_HAEMATOLOGY_SAMPLES.pdf"  # Replace with your PDF file path
output_directory = "splitpdf"  # Replace with your desired output directory
split_pdf_pages_fitz(input_pdf, output_directory)

# PDF Table Extractor

Extracts tables from PDFs to CSV using `tabula-py`.

## Installation

```bash
pip install tabula-py pandas jpype1```

## License

This project is open-source and available for public use.

## Contributing

Feel free to fork this repository, submit pull requests, or report issues!

## Contact

For any questions or suggestions, reach out via GitHub Issues.

