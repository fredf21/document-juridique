# Synthèse Globale - Sprint 02

## 🎯 Objectif Atteint
L'**US02 (Extraction de Texte PDF)** a été complétée. Le système est désormais capable d'extraire le texte brut des PDF textuels et d'afficher un aperçu dans l'interface Streamlit.

## ✅ Succès Marquants
- **Modularisation Réussie** : L'isolation de la logique dans `src/utils/pdf_processor.py` a prouvé la robustesse de l'architecture.
- **Gestion des Erreurs** : L'implémentation de détections pour les fichiers protégés ou vides renforce la fiabilité du MVP.
- **Qualité des Tests** : Le passage à des fichiers PDF d'échantillons réels a permis une validation beaucoup plus précise que les fichiers "dummy".

## ⚠️ Défis & Obstacles
- **Blocages Git** : Des restrictions réseau majeures ont empêché les `push` vers le serveur distant, compliquant le flux de livraison.
- **Limites Techniques** : La dépendance à `PyPDF2` rend l'extraction impossible pour les documents scannés (images sans couche texte).
- **Gestion d'État** : Besoin d'optimiser le cache Streamlit pour éviter les re-processings inutiles lors des interactions UI.

## 🚀 Plan d'Actions (Sprint 03)
1. **Évolution OCR** : Intégrer un module "fallback" (ex: `pytesseract`) pour traiter les PDF non textuels.
2. **Standardisation** : Définir un contrat d'interface (objet standard) pour le texte extrait afin d'alimenter le futur module de résumé.
3. **Infrastructure Git** : Fixer et documenter une méthode de synchronisation robuste pour contourner les blocages réseau.
4. **Stabilité QA** : Explorer des tests unitaires plus granulaires pour pallier l'absence de tests Playwright en environnement restreint.
