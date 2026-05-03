# Changelog

All notable changes to this project will be documented in this file.

## [0.6.0] - 2026-04-13

### Added
- **US06 : Interface Graphique Premium (UI/UX)**
  - Refonte visuelle majeure avec un thème Navy & Gold.
  - Intégration d'une bannière professionnelle générée par IA.
  - Utilisation de Glassmorphism (effets de flou et transparence) pour les conteneurs.
  - Personnalisation avancée des boutons et composants Streamlit via CSS injecté.
  - Amélioration de la hiérarchie visuelle et de la typographie (Playfair Display & Outfit).

## [0.5.0] - 2026-03-24

### Added
- **US05 : Analyse et Visualisation du Score de Confiance**
  - Mise à jour du prompt Gemini pour retourner un format JSON structuré.
  - Intégration d'une jauge de confiance dynamique (`st.progress`) dans l'interface.
  - Codage couleur de la fiabilité (Vert/Orange/Rouge) selon le score.
  - Robustesse accrue du parsing avec gestion des erreurs de format JSON.

## [0.4.0] - 2026-03-24

### Added
- **US04 : Interaction Vocale (TTS - gTTS)**
  - Nouveau service `src/services/audio_service.py` utilisant `gTTS`.
  - Utilisation de `BytesIO` pour une gestion de l'audio 100% en mémoire vive.
  - Intégration d'un bouton de lecture audio dans l'interface Streamlit.
  - Mise en cache des données audio via `@st.cache_data`.

## [0.3.0] - 2026-03-24

### Added
- **US03 : Résumé Automatique par IA (Gemini)**
  - Intégration de `google-generativeai` pour le modèle `gemini-flash-latest`.
  - Service backend `src/services/ai_connector.py` pour générer les résumés.
  - Interface Streamlit pour l'affichage interactif avec gestion sécurisée des clés via `.env`.

## [0.2.0] - 2026-03-08


### Added
- **US02 : Extraction de Texte PDF**
  - Nouveau module `src/utils/pdf_processor.py` utilisant `PyPDF2`.
  - Intégration d'un aperçu du texte extrait dans l'application Streamlit.
  - Gestion des PDF protégés et des documents sans texte (scans).

## [0.1.0] - 2026-02-19

### Added
- **US01 : Import de Document PDF**
  - New Streamlit interface for PDF upload.
  - File size validation (10MB limit).
  - Success feedback and file information display.
  - Visual improvements with custom CSS.

