# Plan de Test Manuel : US01 - Import de Document PDF

Ce document détaille les étapes de vérification manuelle pour la fonctionnalité d'import de document PDF.

## 1. Informations Générales
- **ID de la Story** : US01
- **Fonctionnalité** : Import de Document PDF
- **Testeur** : QA (Antigravity)
- **Date** : 2026-02-19

## 2. Checklist de Test

| ID | Scénario de Test | Étapes de Reproduction | Résultat Attendu | Statut |
| :--- | :--- | :--- | :--- | :--- |
| **01.1** | Import réussi d'un PDF valide | 1. Lancer l'application.<br>2. Sélectionner un fichier PDF de moins de 10 Mo.<br>3. Cliquer sur "Upload". | Message de succès affiché.<br>Nom du fichier affiché. | [ ] |
| **01.2** | Blocage d'un format de fichier non-PDF | 1. Tenter d'importer un fichier `.txt` ou `.jpg`. | L'interface doit empêcher la sélection ou afficher une erreur immédiate. | [ ] |
| **01.3** | Limite de taille de fichier (10 Mo) | 1. Sélectionner un fichier PDF de plus de 10 Mo. | Un message d'erreur "File too large" (ou équivalent) doit s'afficher. | [ ] |
| **01.4** | Affichage du nom du fichier | 1. Charger un PDF valide. | Le nom exact du fichier doit être visible à l'écran. | [ ] |
| **01.5** | Persistance visuelle de l'erreur | 1. Charger un fichier invalide.<br>2. Vérifier que l'erreur reste visible tant qu'un nouveau fichier n'est pas chargé. | Le message d'erreur est clair et reste présent. | [ ] |

## 3. Environnement de Test
- **Navigateur** : Chrome / Firefox / Edge
- **Framework** : Streamlit
- **URL Locale** : http://localhost:8501

## 4. Conclusion
- [ ] Fonctionnalité Validée
- [ ] Bogues Identifiés (Voir section notes ci-dessous)

### Notes / Bogues :
*   (À remplir lors de l'exécution)
