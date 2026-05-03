# Technical Specification: US02 - Extraction de Texte PDF

## 1. Overview
This specification details the extraction of raw text from a PDF document uploaded via the US01 interface. The goal is to provide a clean string of text for future analysis.

## 2. Proposed Stack
- **Framework**: Streamlit.
- **Language**: Python 3.10+.
- **Libraries**:
  - `PyPDF2` (Already in requirements): Primary library for parsing PDF metadata and content.
  - `io`: To handle the file stream from Streamlit.

## 3. Files to Create/Modify
- `src/utils/pdf_processor.py`: [NEW] Utility class to handle text extraction logic.
- `src/app.py`: [MODIFY] Inject the extraction call and display the preview.
- `requirements.txt`: [STABLE] No new dependencies for now.

## 4. Implementation Details

### Extraction Logic (`src/utils/pdf_processor.py`)
- Create a function `extract_text_from_pdf(file_stream)`.
- Use `PyPDF2.PdfReader`.
- Iterate through all pages and concatenate text using `page.extract_text()`.
- **Accents/Encoding**: `PyPDF2` generally handles UTF-8 well, but we should ensure the result is stripped of excessive whitespace.

### Frontend Integration (`src/app.py`)
- After a successful upload (US01), call the extraction utility.
- Add an `st.expander("Aperçu du texte extrait")` to show the first 1000 characters.
- Use `st.text_area` or `st.code` for the preview.

### Validation & Error Handling
- **Empty PDF**: If no text is found, return a specific error/empty message.
- **Protected PDF**: Catch exceptions if the PDF is password-protected and display a user-friendly error.
- **Corrupted PDF**: Use a `try-except` block to catch `PdfReadError`.

## 5. Test Strategy
### Automated Tests
- None at this stage.

### Manual Verification
1. **Standard PDF**: Verify that text (including accents like 'é', 'à') is correctly displayed in the expander.
2. **Protected/Encrypted PDF**: Verify that an error message "Le fichier est protégé par mot de passe" is displayed.
3. **Scan (Image-only) PDF**: If no text is extracted, inform the user that OCR might be needed in a future version.

## 6. Constraints
- Performance: Extraction must be fast enough for a browser-based interaction.
- Security: Do not store the extracted text permanently on disk yet (keep in memory).
