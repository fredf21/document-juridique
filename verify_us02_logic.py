import sys
import os
from io import BytesIO

# Add src to path
sys.path.append(os.path.abspath('src'))

from utils.pdf_processor import extract_text_from_pdf

def test_extraction():
    print("--- Test 1: Valid PDF ---")
    with open('test_valid.pdf', 'rb') as f:
        # Streamlit's file_uploader returns a UploadedFile which has a .read() method
        # and behaves like a file object. Our function expects this.
        text, error = extract_text_from_pdf(f)
        if error:
            print(f"FAILED: {error}")
        else:
            print(f"SUCCESS: Extracted {len(text)} characters.")
            print(f"Preview: {text[:50]}...")

    print("\n--- Test 2: Invalid Format (Text file) ---")
    # Note: extraction function expects a PDF. PyPDF2 will likely fail.
    with open('test_invalid.txt', 'rb') as f:
        text, error = extract_text_from_pdf(f)
        if error:
            print(f"EXPECTED ERROR: {error}")
        else:
            print(f"UNEXPECTED SUCCESS: {text[:50]}")

    print("\n--- Test 3: Large PDF ---")
    with open('test_large.pdf', 'rb') as f:
        text, error = extract_text_from_pdf(f)
        if error:
            print(f"ERROR: {error}")
        else:
            print(f"SUCCESS: Extracted {len(text)} characters.")

if __name__ == "__main__":
    test_extraction()
