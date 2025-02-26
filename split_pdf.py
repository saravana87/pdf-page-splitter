import os
from io import BytesIO
from pdfminer.high_level import extract_pages, extract_text
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import fitz  # PyMuPDF
import os

def split_pdf_pages_fitz(pdf_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    try:
        doc = fitz.open(pdf_path)
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            new_doc = fitz.open()
            new_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)  # Extracts a single page
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
