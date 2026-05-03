# Rétrospective du Sprint 02

## 🤖 Retours des Agents

### [ARCHITECT]
1.  **Qu'est-ce qui a bien fonctionné ?**
    - La **modularisation** de l'extraction (`src/utils/pdf_processor.py`) a prouvé son efficacité : l'architecture a permis au CODER d'implémenter US02 sans impacter la structure globale.
    - L'approche "MVP-First" a permis de livrer une extraction texte fonctionnelle rapidement, confirmant la viabilité de l'infrastructure actuelle.
2.  **Quels ont été les principaux obstacles ou difficultés ?**
    - La transition d'un simple upload (US01) à un **pipeline de données** (US02) a mis en évidence le besoin d'une meilleure gestion d'état dans Streamlit pour éviter les re-traitements inutiles.
    - La découverte de l'incapacité de `PyPDF2` à lire les documents scannés (images) impose une révision de l'architecture pour inclure un module OCR au prochain sprint.
3.  **Quelles actions concrètes pouvons-nous prendre pour le prochain sprint ?**
    - Concevoir un **système de "fallback" (OCR)** intégré au `pdf_processor` pour détecter et traiter les PDF non textuels.
    - Préparer l'architecture pour le module de **Résumé IA** en définissant un contrat d'interface (objet de sortie standardisé) pour le texte extrait.

### [CODER]
1. **Qu'est-ce qui a bien fonctionné ?**
    - L'extraction brute avec `PyPDF2` est rapide et efficace pour les documents textuels standards.
    - La séparation de la logique dans `src/utils/pdf_processor.py` a facilité l'intégration propre dans Streamlit sans encombrer `app.py`.
    - La gestion proactive des erreurs (fichiers protégés, scans vides) permet d'offrir une meilleure expérience utilisateur.
2. **Quels ont été les principaux obstacles ou difficultés ?**
    - **Connectivité Git** : Les problèmes de `push` (Timeouts HTTPS, permissions SSH) ont été l'obstacle majeur de fin de sprint, soulignant un besoin de stabilisation de l'environnement de déploiement.
    - **Limites de l'extraction** : Confirmation que `PyPDF2` ne peut pas lire les PDF "scannés" (images), ce qui exigera une solution OCR à l'avenir.
3. **Quelles actions concrètes pouvons-nous prendre pour le prochain sprint ?**
    - Fixer une configuration Git standardisée (URL HTTP/HTTPS avec jeton) dans la documentation technique.
    - Étudier l'intégration d'un module OCR (ex: `pytesseract`) pour gérer les documents non textuels.


### [QA]
1. **Qu'est-ce qui a bien fonctionné ?**
    - La création du **Plan de Test Manuel** (`US02_test_plan.md`) a permis une couverture complète des cas limites (accents, PDF protégés, documents vides).
    - La validation de la logique d'extraction avec un **vrai PDF échantillon** a confirmé la fiabilité de l'intégration `PyPDF2`.
    - Le remplacement des fichiers "dummy" par des documents valides a significativement amélioré la qualité des données de test.
2. **Quels ont été les principaux obstacles ou difficultés ?**
    - **Fichiers de test invalides** : L'utilisation initiale de faux PDF (fichiers texte renommés) a causé des erreurs de parsing, soulignant la nécessité de tester avec des fichiers structurellement corrects.
    - **Blocage de l'automatisation browser** : L'impossibilité d'exécuter des tests Playwright dans l'environnement actuel limite la validation automatisée de l'interface utilisateur.
3. **Quelles actions concrètes pouvons-nous prendre pour le prochain sprint ?**
    - Intégrer une **détection de PDF "image seule"** pour avertir l'utilisateur dès l'upload (préparation pour l'OCR).
    - Stabiliser l'environnement de test ou adopter une approche de test unitaire plus granulaire pour les utilitaires techniques.
    - Ajouter une étape de **validation d'intégrité du PDF** avant l'extraction pour éviter les erreurs de lecture sur les fichiers corrompus.

### [DEVOPS]
1.  **Qu'est-ce qui a bien fonctionné ?**
    - La gestion locale des branches et des commits a été fluide pour la US02. La capacité à "stager" proprement l'ensemble du projet (incluant les dossiers parents) a été stabilisée.
    - L'initialisation du Sprint 2 a été faite sans délai, permettant à l'équipe de se concentrer immédiatement sur l'extraction de texte.
2.  **Quels ont été les principaux obstacles ou difficultés ?**
    - **Blocages de synchronisation Git** : Les tentatives de push via SSH et via les ports HTTP (80/44310/443) avec PAT ont toutes échoué en raison de restrictions réseau ou de configuration serveur hors de mon contrôle direct.
    - Ce blocage a créé une friction dans le flux de livraison continue (CI/CD), forçant une synchronisation manuelle par l'utilisateur.
3.  **Quelles actions concrètes pouvons-nous prendre pour le prochain sprint ?**
    - **Documentation Git** : Fixer une fois pour toutes la méthode de synchronisation (locale vs distante) dans un guide technique pour éviter de perdre du temps sur des tests de ports répétitifs.
    - **Préparation OCR** : Anticiper l'installation de dépendances système pour `pytesseract` (Tesseract OCR) si cette voie est confirmée par l'Architecte, afin d'éviter des échecs d'installation en plein milieu de sprint.

---

## 📝 Questions Clés pour le Bilan

1. **Qu'est-ce qui a bien fonctionné ?** (Identifiez les forces et les succès de ce sprint).
2. **Quels ont été les principaux obstacles ou difficultés ?** (Qu'est-ce qui a ralenti l'équipe ou causé des frictions ?).
3. **Quelles actions concrètes pouvons-nous prendre pour le prochain sprint ?** (Définissez des points d'amélioration précis).
