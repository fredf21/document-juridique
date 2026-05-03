# Rétrospective du Sprint 05

## 🤖 Retours des Agents

### [ARCHITECT]
1.  **Le passage au format JSON structuré pour Gemini a-t-elle réellement éliminé les erreurs de parsing par rapport au texte brut ?**
    - Oui, le JSON a rendu l'application beaucoup plus résiliente. En forçant le LLM à suivre un schéma strict, on a quasiment éliminé les erreurs "Unexpected Token" ou les cas où l'IA incluait du bavardage avant le résumé. C'est un gain de stabilité majeur pour le backend.
2.  **La jauge de confiance (visualisation) est-elle assez parlante pour aider l'utilisateur à décider de la fiabilité du résumé ?**
    - C'est un excellent premier pas vers la transparence. La jauge permet à l'utilisateur de relativiser l'affirmation de l'IA, surtout sur des documents complexes. Pour le futur, il serait intéressant d'expliquer *pourquoi* le score est bas (ex: manque de contexte, texte illisible).
3.  **Quels autres indicateurs (complexité, ton, risques) apporteraient une valeur complémentaire à ce score global ?**
    - Un **score de complexité juridique** (niveau de jargon) aiderait à savoir si le résumé a vraiment simplifié le texte. De plus, un **indicateur de risques** (clauses litigieuses) serait la suite logique pour apporter une réelle valeur métier au grand public.

### [CODER]
1.  **Le passage au format JSON structuré pour Gemini a-t-il réellement éliminé les erreurs de parsing par rapport au texte brut ?**
    - Absolument. En utilisant `json.loads` avec un nettoyage des balises Markdown (` ```json `), on a obtenu une extraction beaucoup plus fiable. Cela permet de séparer proprement le contenu (résumé) des métadonnées (score), ce qui était périlleux avec du texte brut.
2.  **La jauge de confiance (visualisation) est-elle assez parlante pour aider l'utilisateur à décider de la fiabilité du résumé ?**
    - L'utilisation de `st.progress` combinée à des couleurs HTML personnalisées (`st.markdown`) rend l'indicateur très intuitif. L'utilisateur comprend immédiatement s'il doit être vigilant ou s'il peut faire confiance au résultat au premier coup d'œil.
3.  **Quels autres indicateurs (complexité, ton, risques) apporteraient une valeur complémentaire à ce score global ?**
    - Un **score de lisibilité** (Gunning Fog ou similaire, adapté au français) serait utile pour quantifier l'effort de simplification. Techniquement, demander à l'IA d'identifier des **mots-clés complexes** et d'en donner une définition simple en infobulle serait également une grande amélioration.


### [QA]
1.  **Le passage au format JSON structuré pour Gemini a-t-il réellement éliminé les erreurs de parsing par rapport au texte brut ?**
    - Absolument. Du point de vue QA, la validation du format JSON via `verify_us05_logic.py` a démontré une robustesse exemplaire. Le système gagne en prévisibilité : on peut désormais tester séparément la qualité du texte et la validité du score numérique, ce qui était impossible auparavant.
2.  **La jauge de confiance (visualisation) est-elle assez parlante pour aider l'utilisateur à décider de la fiabilité du résumé ?**
    - Oui, l'aspect visuel (couleurs dynamiques dans Streamlit) est très efficace. Durant les tests, le score de 100% sur le PDF factice a prouvé que l'IA sait s'auto-évaluer avec justesse. La gestion du cas d'erreur (score par défaut à 50% en cas de JSON malformé) assure également une continuité de service.
3.  **Quels autres indicateurs (complexité, ton, risques) apporteraient une valeur complémentaire à ce score global ?**
    - Un **indicateur de "sources citées"** (extraits de texte brut justifiant le résumé) permettrait de réduire la sensation de "boîte noire". Techniquement, j'ai identifié et corrigé une **régression critique** (import manquant) durant ce sprint; il sera crucial d'ajouter des tests de fumée (Smoke Tests) automatisés pour éviter que de futures modifications ne cassent la chaîne d'appel à l'IA.

### [DEVOPS]
1.  **Le passage au format JSON structuré pour Gemini a-t-il réellement éliminé les erreurs de parsing par rapport au texte brut ?**
    - Absolument. Du point de vue DevOps, le JSON est le standard d'échange par excellence. Cela a supprimé le besoin de regex complexes et fragiles pour tenter d'isoler le score du texte. La chaîne de traitement est désormais beaucoup plus stable et "maintenable", avec une séparation claire entre les données métier et les métadonnées techniques.
2.  **La jauge de confiance (visualisation) est-elle assez parlante pour aider l'utilisateur à décider de la fiabilité du résumé ?**
    - Oui, c'est une excellente pratique de transparence. En termes de performance, cette visualisation légère ne ralentit pas l'interface Streamlit. Cela renforce l'aspect "professionnel" de l'application tout en restant simple à déployer.
3.  **Quels autres indicateurs (complexité, ton, risques) apporteraient une valeur complémentaire à ce score global ?**
    - Un **score de coût/token** (invisible pour l'utilisateur mais utile en monitoring) nous permettrait de suivre l'efficacité de nos prompts. Sur le plan métier, un **indicateur de complétude** (est-ce que tout le PDF a été traité ?) serait un complément idéal au score de confiance pour rassurer pleinement l'utilisateur.

---

## 📝 Questions Clés pour le Bilan

1.  **Le passage au format JSON structuré pour Gemini a-t-il réellement éliminé les erreurs de parsing par rapport au texte brut ?**
2.  **La jauge de confiance (visualisation) est-elle assez parlante pour aider l'utilisateur à décider de la fiabilité du résumé ?**
3.  **Quels autres indicateurs (complexité, ton, risques) apporteraient une valeur complémentaire à ce score global ?**
