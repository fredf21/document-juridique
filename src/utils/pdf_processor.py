import PyPDF2
from io import BytesIO

def extract_text_from_pdf(uploaded_file):
    """
    Extracts raw text from a PDF file stream.
    
    Args:
        uploaded_file: A file-like object (e.g., from Streamlit's file_uploader).
        
    Returns:
        tuple: (extracted_text, error_message)
    """
    text = ""
    error = None
    
    try:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(BytesIO(uploaded_file.read()))
        
        # Reset file pointer for future use strictly if needed, 
        # but here we read the whole content into BytesIO
        
        if reader.is_encrypted:
            return None, "Le fichier est protégé par mot de passe."
            
        # Iterate through all pages
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        
        if not text.strip():
            return None, "Aucun texte détecté dans le document (il s'agit peut-être d'un scan)."
            
    except Exception as e:
        error = f"Une erreur est survenue lors de l'extraction : {str(e)}"
        return None, error
        
    return text.strip(), None
