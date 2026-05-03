import streamlit as st
import os
from utils.pdf_processor import extract_text_from_pdf

from dotenv import load_dotenv
from services.ai_connector import summarize_text
from services.audio_service import generate_audio_bytes

# Load environment variables (e.g., GEMINI_API_KEY from .env)
load_dotenv()

# App configuration
st.set_page_config(
    page_title="Analyseur de Documents Juridiques",
    page_icon="⚖️",
    layout="centered"
)

# Custom CSS for a premium look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Outfit:wght@300;400;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    
    .main-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 24px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        margin-bottom: 2rem;
    }

    h1 {
        font-family: 'Playfair Display', serif;
        color: #d4af37;
        font-size: 3rem !important;
        text-align: center;
        margin-bottom: 0.5rem !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }

    h3 {
        font-family: 'Outfit', sans-serif;
        color: #94a3b8;
        text-align: center;
        font-weight: 300 !important;
        letter-spacing: 1px;
    }

    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background: linear-gradient(90deg, #d4af37 0%, #f1c40f 100%);
        color: #1a2a6c;
        font-weight: 700;
        font-family: 'Outfit', sans-serif;
        border: none;
        padding: 0.75rem;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(212, 175, 55, 0.5);
        color: #1a2a6c;
        background: linear-gradient(90deg, #f1c40f 0%, #d4af37 100%);
    }

    .stProgress > div > div > div > div {
        background-color: #d4af37;
    }

    .reportview-container .main .block-container {
        max-width: 900px;
    }

    .stExpander {
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
    }

    /* Custom labels for sentiment/confidence */
    .confidence-label {
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def get_audio(text: str):
    """Generates audio for the given text and caches the result."""
    return generate_audio_bytes(text)

def main():
    # Banner Integration
    banner_path = os.path.join("src", "assets", "legal_synthesizer_banner.png")
    if os.path.exists(banner_path):
        st.image(banner_path, use_container_width=True)
    
    st.title("⚖️ Legal Synthesizer Pro")
    st.markdown("### L'intelligence artificielle au service de votre compréhension juridique")
    st.write("---")

    # Ensure API Key is loaded
    api_key = os.environ.get("GEMINI_API_KEY")

    with st.container():
        st.markdown('<div class="main-container">', unsafe_allow_html=True)
        # File uploader
        uploaded_file = st.file_uploader(
            "Déposez votre document PDF ici",
            type=['pdf'],
            help="Analyse sécurisée des fichiers jusqu'à 10 Mo."
        )
        st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_file is not None:
        # Size validation (10MB limit)
        max_size = 10 * 1024 * 1024  # 10 MB in bytes
        
        if uploaded_file.size > max_size:
            st.error("❌ Le fichier est trop volumineux. La taille maximale autorisée est de 10 Mo.")
        else:
            # Success feedback for upload
            st.success(f"✅ Document '{uploaded_file.name}' prêt pour analyse.")
            
            # Clear previous summary if a new file is uploaded
            if 'last_uploaded_file' not in st.session_state or st.session_state.last_uploaded_file != uploaded_file.name:
                st.session_state.last_uploaded_file = uploaded_file.name
                if 'summary' in st.session_state:
                    del st.session_state.summary
                if 'score' in st.session_state:
                    del st.session_state.score
            
            # Extraction logic
            with st.spinner("Extraction des clauses juridiques..."):
                text, error = extract_text_from_pdf(uploaded_file)
            
            if error:
                st.error(f"❌ {error}")
            else:
                st.balloons()
                
                with st.container():
                    st.markdown('<div class="main-container">', unsafe_allow_html=True)
                    st.markdown("#### 📄 Informations du Document")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.info(f"**Nom :** {uploaded_file.name}")
                    with col2:
                        st.info(f"**Taille :** {uploaded_file.size / 1024 / 1024:.2f} Mo")
                    
                    with st.expander("🔍 Voir le texte brut extrait"):
                        st.text_area("", value=text, height=200, disabled=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                
                # AI Analysis Section
                if not api_key:
                    st.warning("⚠️ Configuration manquante : GEMINI_API_KEY non détectée.")
                else:
                    with st.container():
                        st.markdown('<div class="main-container">', unsafe_allow_html=True)
                        if st.button("✨ LANCER L'ANALYSE INTELLIGENTE"):
                            with st.spinner("Analyse par l'IA en cours..."):
                                summary, score, auth_error = summarize_text(text, api_key)
                                
                            if auth_error:
                                st.error(auth_error)
                            else:
                                st.success("Analyse terminée !")
                                st.session_state.summary = summary
                                st.session_state.score = score
                        st.markdown('</div>', unsafe_allow_html=True)
                                    
                    # Display Results Card
                    if 'summary' in st.session_state:
                        with st.container():
                            st.markdown('<div class="main-container">', unsafe_allow_html=True)
                            st.markdown("### 📊 Rapport de Fiabilité")
                            
                            score = st.session_state.get('score', 0)
                            
                            if score >= 80:
                                label = "🟢 TRÈS FIABLE"
                                color = "#d4af37"
                            elif score >= 50:
                                label = "🟠 FIABILITÉ MOYENNE"
                                color = "#f39c12"
                            else:
                                label = "🔴 PRUDENCE RECOMMANDÉE"
                                color = "#e74c3c"
                            
                            st.markdown(f'<div class="confidence-label" style="color:{color};">{label} ({score}%)</div>', unsafe_allow_html=True)
                            st.progress(score / 100)
                            
                            st.markdown("---")
                            st.markdown("### 📝 Résumé de l'Expert IA")
                            st.markdown(f'<div style="background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 12px; border-left: 4px solid #d4af37; font-family: \'Outfit\', sans-serif;">{st.session_state.summary}</div>', unsafe_allow_html=True)

                            st.write("")
                            if st.button("🔊 ÉCOUTER LE RÉSUMÉ VOCAL"):
                                with st.spinner("Préparation de la synthèse vocale..."):
                                    audio_buffer = get_audio(st.session_state.summary)
                                if audio_buffer:
                                    st.audio(audio_buffer, format="audio/mp3")
                                else:
                                    st.warning("⚠️ Service vocal indisponible.")
                            st.markdown('</div>', unsafe_allow_html=True)



if __name__ == "__main__":
    main()
