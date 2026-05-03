# Plan de Test Manuel : US04 - Interaction Vocale (TTS)

Ce document détaille les étapes de vérification manuelle pour la fonctionnalité de synthèse vocale du résumé.

## 1. Informations Générales
- **ID de la Story** : US04
- **Fonctionnalité** : Interaction Vocale (Text-to-Speech)
- **Testeur** : QA (Antigravity)
- **Date** : 2026-03-24

## 2. Checklist de Test

| ID | Scénario de Test | Étapes de Reproduction | Résultat Attendu | Statut |
| :--- | :--- | :--- | :--- | :--- |
| **04.1** | Présence du bouton Audio | 1. Importer un PDF et générer un résumé (US03).<br>2. Vérifier la présence du bouton "🔊 Écouter le résumé". | Le bouton est visible à côté du résumé. | [ ] |
| **04.2** | Génération et Lecture Audio | 1. Cliquer sur "🔊 Écouter le résumé".<br>2. Attendre la fin du chargement. | Un lecteur audio apparaît.<br>L'audio commence ou est prêt à être lu. | [ ] |
| **04.3** | Qualité de la voix (Français) | 1. Écouter l'audio généré. | La voix est claire et s'exprime en français.<br>Les accents sont correctement prononcés. | [ ] |
| **04.4** | Gestion du Cache | 1. Cliquer une deuxième fois sur le bouton d'écoute.<br>2. Vérifier si le temps de chargement est réduit. | L'audio est disponible quasi-instantanément (via `@st.cache_data`). | [ ] |
| **04.5** | Contrôles du Lecteur | 1. Utiliser les fonctions pause, volume et défilement du lecteur natif. | Toutes les fonctions du lecteur Streamlit (`st.audio`) sont opérationnelles. | [ ] |
| **04.6** | Cas d'erreur (Service indisponible) | 1. Simuler une coupure réseau ou quota gTTS dépassé (si possible). | Message d'avertissement : "⚠️ Le service vocal est temporairement indisponible." | [ ] |

## 3. Environnement de Test
- **Navigateur** : Chrome / Firefox / Edge
- **Moteur TTS** : gTTS (Google Text-to-Speech)
- **Format Audio** : MP3 (via BytesIO)

## 4. Conclusion
- [ ] Fonctionnalité Validée
- [ ] Bogues Identifiés

### Notes / Bogues :
*   (À remplir lors de l'exécution)
