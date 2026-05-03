# Plan de Test Manuel : US02 - Extraction de Texte PDF (OCR/Parsing)

Ce document détaille les étapes de vérification manuelle pour la fonctionnalité d'extraction de texte à partir de documents PDF.

## 1. Informations Générales
- **ID de la Story** : US02
- **Fonctionnalité** : Extraction de Texte PDF
- **Testeur** : QA (Antigravity)
- **Date** : 2026-03-08

## 2. Checklist de Test

| ID | Scénario de Test | Étapes de Reproduction | Résultat Attendu | Statut |
| :--- | :--- | :--- | :--- | :--- |
| **02.1** | Extraction réussie d'un PDF texte standard | 1. Charger un PDF contenant du texte.<br>2. Cliquer sur l'expander "Aperçu du texte extrait". | Le texte du PDF est affiché.<br>Le texte est lisible et fidèle. | [ ] |
| **02.2** | Gestion correcte des accents | 1. Charger un PDF contenant des accents (é, à, ç, etc.).<br>2. Vérifier le texte dans l'aperçu. | Les caractères accentués sont correctement affichés. | [ ] |
| **02.3** | Limitation de l'aperçu (1000 chars) | 1. Charger un PDF long (> 2000 caractères).<br>2. Vérifier la longueur de l'aperçu. | L'aperçu affiche les 1000 premiers caractères. | [ ] |
| **02.4** | PDF protégé par mot de passe | 1. Tenter de charger un PDF protégé.<br>2. Vérifier le message d'erreur. | Message : "Le fichier est protégé par mot de passe" (ou équivalent). | [ ] |
| **02.5** | PDF "Scan" (uniquement des images) | 1. Charger un PDF qui est un scan d'un document (pas de texte sélectionnable). | Message informant que l'OCR sera nécessaire ou que le texte est vide. | [ ] |
| **02.6** | PDF Corrompu | 1. Charger un fichier PDF altéré. | Message d'erreur technique clair (ex: "Erreur lors de la lecture du PDF"). | [ ] |

## 3. Environnement de Test
- **Navigateur** : Chrome / Firefox / Edge
- **Framework** : Streamlit
- **Bibliothèque** : PyPDF2

## 4. Conclusion
- [ ] Fonctionnalité Validée
- [ ] Bogues Identifiés

### Notes / Bogues :
*   (À remplir lors de l'exécution)
