# Rétrospective du Sprint 01

## 🤖 Retours des Agents

### [ARCHITECT]
1.  **Qu'est-ce qui a bien fonctionné ?**
    - Le choix de **Streamlit** pour l'US01 a permis de définir une architecture simple et efficace pour l'upload de PDF, parfaitement alignée avec le besoin de MVP.
    - La documentation de la spécification technique dans `docs/specs/US01_spec.md` a fourni une feuille de route claire, séparant bien l'interface de la validation.
2.  **Quels ont été les principaux obstacles ou difficultés ?**
    - Équilibrer la simplicité du MVP avec les futures capacités d'analyse IA (nécessité de ne pas restreindre l'architecture trop tôt).
    - Définition des limites de taille (10 Mo) qui pourraient varier selon la complexité des futurs documents juridiques.
3.  **Quelles actions concrètes pouvons-nous prendre pour le prochain sprint ?**
    - Anticiper la structure des données extraites pour faciliter l'intégration de la fonctionnalité de "Résumé Automatique".
    - Standardiser un format de réponse pour les erreurs de validation afin que le `[CODER]` puisse les implémenter uniformément.

### [CODER]
1.  **Qu'est-ce qui a bien fonctionné ?**
    - **Streamlit** a permis un prototypage ultra-rapide avec une gestion native fluide de l'upload de fichiers.
    - L'injection de **CSS personnalisé** a permis d'obtenir un rendu "premium" (glassmorphism/gradients) dès le premier jet, améliorant l'expérience utilisateur perçue.
    - La validation logicielle du poids des fichiers (<10 Mo) a été intégrée directement dans le flux d'upload sans friction.
2.  **Quels ont été les principaux obstacles ou difficultés ?**
    - Le ciblage précis des éléments Streamlit en CSS peut être fragile car dépendant des classes générées par le framework.
    - Gérer les retours d'erreurs visuels de manière élégante tout en restant dans les limites du composant `st.file_uploader`.
3.  **Quelles actions concrètes pouvons-nous prendre pour le prochain sprint ?**
    - Externaliser la logique de traitement des PDF dans un module `src/utils/` pour éviter que `app.py` ne devienne trop volumineux.
    - Définir un thème Streamlit (`.streamlit/config.toml`) pour centraliser les styles visuels plutôt que de les injecter par blocs Markdown.


### [QA]
1.  **Qu'est-ce qui a bien fonctionné ?**
    - La création d'un **Plan de Test Manuel** structuré dans `docs/reports/` a permis de couvrir tous les critères d'acceptation de l'US01 (format, taille, feedback).
    - La génération proactive de **fichiers de test** (`valid`, `invalid`, `large`) facilite grandement la répétabilité des tests manuels.
    - L'utilisation de tests de connectivité HTTP (curl/requests) a permis de confirmer la disponibilité de l'application malgré des échecs d'outils plus complexes.
2.  **Quels ont été les principaux obstacles ou difficultés ?**
    - Échec de la **vérification automatisée** via le navigateur/Playwright en raison d'une configuration d'environnement manquante ($HOME). Cela a retardé la validation automatisée de l'UI.
    - Dépendance aux tests manuels pour valider le rendu visuel et les interactions Streamlit.
3.  **Quelles actions concrètes pouvons-nous prendre pour le prochain sprint ?**
    - Collaborer avec l'équipe **[DEVOPS]** pour stabiliser l'environnement de test automatisé (Playwright/Browser).
    - Explorer des outils de test plus légers ou spécifiques à Streamlit pour automatiser une partie de la validation sans passer par un navigateur complet.
    - Intégrer la validation des fichiers (via `PyPDF2` par exemple) dans le plan de test pour s'assurer que le contenu est réellement lisible par la future IA.

### [DEVOPS]
1.  **Qu'est-ce qui a bien fonctionné ?**
    - L'initialisation du socle technique (branchement git, gestion des dépendances via `requirements.txt`) a permis au codeur de démarrer sans délai.
    - Le processus de clôture (merge, update du CHANGELOG et du backlog) a été fluide, assurant une branche `main` toujours propre et documentée.
2.  **Quels ont été les principaux obstacles ou difficultés ?**
    - Des problèmes de configuration d'environnement (variable `$HOME` manquante) ont bloqué les tests automatisés du QA via le navigateur.
    - La gestion manuelle du `requirements.txt` pourrait devenir une source d'erreurs avec l'ajout de nouvelles dépendances.
3.  **Quelles actions concrètes pouvons-nous prendre pour le prochain sprint ?**
    - Configurer correctement l'environnement de test (variables d'environnement système) pour permettre au QA d'utiliser les outils de navigation automatisée.
    - Mettre en place la configuration centralisée de Streamlit via `.streamlit/config.toml` pour harmoniser le design sans surcharger le code source.

---

## 📝 Questions Clés pour le Bilan

1.  **Qu'est-ce qui a bien fonctionné ?** (Identifiez les forces et les succès de ce sprint).
2.  **Quels ont été les principaux obstacles ou difficultés ?** (Qu'est-ce qui a ralenti l'équipe ou causé des frictions ?).
3.  **Quelles actions concrètes pouvons-nous prendre pour le prochain sprint ?** (Définissez des points d'amélioration précis).
