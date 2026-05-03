# Spécification Technique - US03 : Résumé Automatique par IA

## 1. Objectif
Définir l'architecture et les détails d'implémentation pour l'intégration d'un modèle de langage (LLM) afin de résumer le contenu des PDF juridiques.

## 2. Choix Technologiques
- **Fournisseur d'IA** : **Google Gemini** (via le SDK `google-generativeai`).
- **Modèle recommandé** : `gemini-1.5-flash` (rapide et efficace pour les tâches de résumé de texte).
- **Service Backend** : Création d'un module dédié dans `src/services/ai_connector.py` pour encapsuler la logique d'appel à l'API.

## 3. Gestion de l'Authentification
- L'API Key de Google (`GEMINI_API_KEY`) doit être stockée de manière sécurisée dans un fichier `.env` à la racine du projet, qui ne sera jamais commité (`.gitignore`).
- Utiliser la bibliothèque `python-dotenv` pour charger ces variables dans le code.

## 4. Architecture du Service (`src/services/ai_connector.py`)
Le service devra exposer une fonction `summarize_text(text: str, api_key: str) -> str`:
1. Configuration de la bibliothèque cliente avec la clé fournie.
2. Construction du prompt système contraignant (voir section 5).
3. Envoi de la requête au modèle.
4. Gestion des exceptions (ex: quota dépassé, erreur réseau, contenu bloqué par sécurité).

## 5. Ingénierie de Prompt (Prompt Design)
Le prompt structuré doit intégrer le contexte et le texte extrait :

```text
Tu es un expert juridique assistant le grand public.
Ton rôle est d'analyser le document juridique suivant et d'en faire un résumé clair, concis et compréhensible par une personne sans formation juridique.

Identifie :
1. La nature du document (ex: Contrat de travail, Bail).
2. Les parties prenantes.
3. Les 3 à 5 points les plus importants à retenir.
4. Les obligations ou risques majeurs (si applicables).

Texte du document :
{text}
```

## 6. Intégration Streamlit (`src/app.py`)
- S'assurer que les variables d'environnement (`load_dotenv()`) sont chargées au démarrage.
- Ajouter un bouton "Générer le Résumé" disponible uniquement si du texte a été extrait.
- Utiliser `st.spinner("Analyse du document par l'IA...")` pendant l'appel réseau.
- Afficher le résultat dans un panneau visuel distinct (`st.success` ou `st.info`).
- Gérer les erreurs via `st.error` (ex: "Clé d'API invalide ou document trop long").
