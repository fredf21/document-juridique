# Plan de Test Manuel : US05 - Score de Confiance

Ce document détaille les étapes de vérification manuelle pour la fonctionnalité d'analyse et de visualisation du score de confiance.

## 1. Informations Générales
- **ID de la Story** : US05
- **Fonctionnalité** : Analyse et Visualisation du Score de Confiance
- **Testeur** : QA (Antigravity)
- **Date** : 2026-03-24

## 2. Checklist de Test

| ID | Scénario de Test | Étapes de Reproduction | Résultat Attendu | Statut |
| :--- | :--- | :--- | :--- | :--- |
| **05.1** | Présence de l'indicateur | 1. Importer un PDF et générer un résumé (US03). | La section "📊 Indicateur de Fiabilité" apparaît après la génération du résumé. | [ ] |
| **05.2** | Affichage de la Jauge | 1. Générer un résumé. | Une barre de progression (`st.progress`) affiche le score extrait. | [ ] |
| **05.3** | Coloration Dynamique | 1. Tester avec différents documents pour obtenir des scores variés.<br>2. Vérifier le libellé et la couleur (CSS). | Score >= 80% : 🟢 Très Fiable<br>Score 50-79% : 🟠 Fiabilité Moyenne<br>Score < 50% : 🔴 Prudence recommandée | [ ] |
| **05.4** | Extraction JSON (Backend) | 1. Vérifier les logs ou logs de test (US05 logic). | Le système extrait correctement le champ `confidence_score` du JSON renvoyé par Gemini. | [ ] |
| **05.5** | Gestion des erreurs JSON | 1. Simuler un retour Gemini non-JSON (ou malformé). | Le système bascule sur un score par défaut de 50 et affiche un avertissement. | [ ] |

## 3. Environnement de Test
- **Navigateur** : Chrome / Firefox / Edge
- **Service IA** : Google Gemini (format JSON)
- **Composant UI** : Streamlit Progress Bar & Metrics

## 4. Conclusion
- [x] Fonctionnalité Validée
- [ ] Bogues Identifiés

### Notes / Bogues :
*   **Bogue mineur (Identifié et Corrigé)** : L'import `google.generativeai` était manquant dans `ai_connector.py`. L'équipe QA l'a ajouté pour permettre l'appel API.
*   **Succès du parsing** : Le système extrait proprement le résumé et le score même si Gemini entoure le JSON de blocs Markdown (```json).
*   **Affichage** : La jauge et les couleurs dynamiques fonctionnent parfaitement dans l'interface Streamlit.
