# User Stories - Sprints 1, 2, 3, 4, 5 & 6

## US01 : Import de Document PDF
**En tant que** : Utilisateur du grand public  
**Je veux** : Pouvoir charger un fichier PDF depuis mon ordinateur vers l'application  
**Afin de** : Permettre au système de l'analyser et d'en extraire les informations clés.

### Critères d'Acceptation
1. **Format de fichier** : L'interface n'accepte que les fichiers au format `.pdf`.
2. **Taille maximale** : Une limite de taille (ex: 10 Mo) est imposée pour éviter les abus.
3. **Confirmation visuelle** : L'utilisateur voit un message de succès après l'upload.
4. **Gestion d'erreur** : Un message clair s'affiche si le fichier est corrompu ou d'un mauvais format.
5. **Prévisualisation** : (Optionnel pour MVP) Le nom du fichier chargé est affiché à l'écran.

---

## US02 : Extraction de Texte PDF (OCR/Parsing)
**En tant que** : Système de traitement  
**Je veux** : Extraire tout le texte contenu dans le PDF chargé  
**Afin de** : Préparer les données pour le résumé et l'analyse ultérieure.

### Critères d'Acceptation
1. **Extraction brute** : Le système doit pouvoir lire le texte d'un PDF standard.
2. **Gestion de l'encodage** : Les caractères spéciaux (accents) doivent être correctement récupérés.
3. **Affichage technique** : L'utilisateur (ou le développeur en phase de test) peut voir un aperçu du texte extrait dans l'interface.
4. **Gestion des erreurs** : Si le texte ne peut pas être extrait (ex: document protégé ou vide), un message d'erreur est affiché.

---

## US03 : Résumé Automatique par IA
**En tant que** : Utilisateur du grand public  
**Je veux** : Obtenir un résumé clair et concis du document juridique chargé  
**Afin de** : Comprendre rapidement les grandes lignes sans avoir à lire tout le jargon technique.

### Critères d'Acceptation
1. **Appel API** : Le système envoie le texte extrait (US02) à un LLM (Gemini ou OpenAI) de manière sécurisée.
2. **Prompt Spécifique** : L'IA reçoit une instruction système stricte pour synthétiser le texte en langage simple (niveau grand public).
3. **Affichage du Résumé** : Le résumé généré est affiché dans l'interface utilisateur de manière lisible.
4. **Gestion de la Limite de Tokens** : (MVP) Si le document est trop long pour le LLM, un message d'erreur clair informe l'utilisateur de la limitation technique actuelle.
5. **Indicateur de Chargement** : L'utilisateur voit un "spinner" ou une barre de progression pendant que l'IA réfléchit.

---

## US04 : Interaction Vocale (Text-to-Speech)
**En tant que** : Utilisateur du grand public  
**Je veux** : Pouvoir écouter le résumé du document généré par l'IA  
**Afin de** : Prendre connaissance des informations importantes sans avoir à lire l'écran (accessibilité et confort).

### Critères d'Acceptation
1. **Bouton de Lecture** : Un bouton "Écouter le résumé" est disponible à côté du texte généré par l'IA.
2. **Génération Audio** : Le système utilise une bibliothèque (ex: `gTTS`) pour convertir le texte du résumé en fichier audio.
3. **Lecteur Audio** : Un lecteur audio natif Streamlit permet de lancer, mettre en pause et ajuster le volume du résumé.
4. **Langue** : La synthèse vocale doit être configurée en français.
5. **Gestion du cache** : (Optionnel MVP) Le fichier audio ne doit être généré qu'une seule fois par résumé pour économiser les ressources.

---

## US05 : Analyse et Visualisation du Score de Confiance
**En tant que** : Utilisateur du grand public  
**Je veux** : Visualiser un score de confiance (fiabilité) du résumé généré par l'IA  
**Afin de** : Évaluer la crédibilité des informations simplifiées qui me sont présentées.

### Critères d'Acceptation
1. **Extraction du Score** : Le système demande au LLM d'évaluer sa propre certitude sur le résumé produit (score de 0 à 100).
2. **Affichage par Jauge** : Le score est affiché visuellement sous forme de jauge colorée (ex: Vert pour >80%, Orange pour 50-80%, Rouge pour <50%).
3. **Libellé de Fiabilité** : Un texte explicatif accompagne la jauge (ex: "Fiabilité : Très élevée").
4. **Mise à jour dynamique** : La jauge s'anime ou s'affiche dès que le résumé est prêt.

---

## US06 : Interface Graphique Premium (UI/UX)
**En tant que** : Utilisateur du grand public  
**Je veux** : Utiliser une interface belle, ergonomique et visuellement professionnelle  
**Afin de** : Avoir confiance en l'outil et naviguer facilement entre les fonctionnalités.

### Critères d'Acceptation
1. **Bannière & Logo** : Une bannière ou un logo distinctif est présent en haut de l'application.
2. **Cohérence Visuelle** : La palette de couleurs est harmonieuse (ex: tons bleus juristes) et appliquée à tous les composants.
3. **Typographie** : Utilisation d'une police moderne (ex: sans-serif) pour une meilleure lisibilité.
4. **Micro-animations** : Des effets de transition ou de survol (hover) enrichissent l'expérience interactive.
5. **Responsive Design** : L'interface s'adapte proprement aux différentes tailles d'écran (Desktop/Mobile).

