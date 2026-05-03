# Technical Specification: US01 - Import de Document PDF

## 1. Overview
This specification details the implementation of the PDF document upload feature. The goal is to allow users to upload a PDF file which will be used for later analysis.

## 2. Proposed Stack
- **Framework**: [Streamlit](https://streamlit.io/) (Simplified UI/UX for AI applications).
- **Language**: Python 3.10+.
- **Libraries**:
  - `streamlit`: For the web interface.
  - `PyPDF2`: To validate file integrity (optional but recommended).

## 3. Files to Create/Modify
- `src/app.py`: [NEW] Main application file containing the upload logic and UI.
- `requirements.txt`: [NEW] Project dependencies.

## 4. Implementation Details

### Frontend (Streamlit)
- Use `st.file_uploader` with `type=['pdf']`.
- Display a success message using `st.success` once the upload is completed.
- Display the filename using `st.info` or `st.write`.

### Validation Logic
- **Format**: Enforced by the file uploader component (only `.pdf`).
- **Size**: Check `file.size` and ensure it is less than 10MB (10,485,760 bytes).
- **Error Handling**: If size exceeds limit, display `st.error`.

## 5. Test Strategy
### Automated Tests
- None planned for this initial MVP phase (Streamlit is primarily tested manually).

### Manual Verification
1. **Valid Upload**:
   - Select a PDF file < 10MB.
   - Result: File name appears, success message shown.
2. **Invalid Format**:
   - Attempt to drag/drop a `.txt` or `.jpg` file.
   - Result: Interface should block or show error.
3. **Invalid Size**:
   - Attempt to upload a PDF > 10MB.
   - Result: Error message displays "File too large".

## 6. Constraints
- Must be compatible with standard web browsers.
- Local storage for uploaded files (temporary for this US).
