import json
import google.generativeai as genai

def summarize_text(text: str, api_key: str) -> tuple:
    """
    Summarizes legal document text using Google Gemini and returns a confidence score.
    
    Args:
        text (str): The raw text extracted from the PDF.
        api_key (str): The Google Gemini API key.
        
    Returns:
        tuple: (summary_text, confidence_score, error_message)
    """
    if not api_key:
        return None, None, "Erreur : La clé d'API (GEMINI_API_KEY) est introuvable."
        
    try:
        # Configuration of the Gemini API client
        genai.configure(api_key=api_key)
        
        # We use the fast and efficient flash model as recommended
        model_name = "gemini-flash-latest"
        model = genai.GenerativeModel(model_name)

        system_prompt = """
Tu es un expert juridique assistant le grand public.
Ton rôle est d'analyser le document juridique suivant et d'en faire un résumé clair, concis et compréhensible par une personne sans formation juridique.

Tu dois impérativement répondre au format JSON suivant :
{
  "summary": "Le texte du résumé avec la nature du document, les parties prenantes, les 3-5 points clés et les risques majeurs.",
  "confidence_score": 85
}

Le score de confiance doit être un entier entre 0 et 100 représentant ton estimation de la fiabilité et de l'exactitude des informations extraites.
"""
        # We append the text directly
        full_prompt = f"{system_prompt}\n\nTexte du document :\n{text}"
        
        # Generate the content
        response = model.generate_content(full_prompt)
        
        if response.text:
            try:
                # Attempt to parse as JSON
                # Sometimes LLMs wrap JSON in markdown blocks, so we clean it up
                content = response.text.strip()
                if content.startswith("```json"):
                    content = content[7:-3].strip()
                elif content.startswith("```"):
                    content = content[3:-3].strip()
                    
                data = json.loads(content)
                summary = data.get("summary", "Résumé non disponible.")
                score = data.get("confidence_score", 0)
                return summary, score, None
            except json.JSONDecodeError:
                # Fallback if the model doesn't return valid JSON
                return response.text, 50, "Avertissement : Le format JSON n'a pas pu être parsé. Score de confiance par défaut (50)."
        else:
            return None, None, "Erreur : Le modèle n'a généré aucun contenu."
            
    except Exception as e:
        error_msg = f"Une erreur réseau ou d'API est survenue lors de la communication avec l'IA. Détails: {str(e)}"
        return None, None, error_msg
