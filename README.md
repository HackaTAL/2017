![HACKATAL 2017](https://raw.githubusercontent.com/HackaTAL/2017/gh-pages/hackatal2017.jpg)

# HackaTAL 2017
---------------
**(hackathon dans le domaine du TAL)**

### TL;DR

Tâches : résumé d’avis et commentaires / prédiction de brevets  
Site web : http://hackatal.github.io/2017  
Dates : 24 au 26 juin 2017  
Lieu : Lab’O, 1 Avenue du Champ de Mars, Orléans, le-lab-o.fr  
Inscrivez-vous (gratuit mais obligatoire) : https://goo.gl/forms/tbFdKosMNNKdPhaH3  

### Description

Dans le cadre de la conférence TALN-RECITAL 2017, sera organisée la seconde édition du HackaTAL, le hackathon dédié à des problématiques liées au TAL. L’objectif est de réunir la communauté autour de défis à relever à l’aide de données et briques logicielles, en consacrant le weekend à modéliser, prototyper, coder, expérimenter, développer, tester, évaluer, comparer, échanger, etc. - par équipes et dans une ambiance décontractée :)

Les tâches proposées concernent cette année le résumé automatique de description de produits à partir de leurs commentaires et la prédiction automatique de la brevetabilité de termes liés à des technologies selon leur historique. L’événement est ouvert à tous, ne nécessite pas de préparation particulière (sauf d’amener sa machine) et ne requiert pas de compétences spécifiques aux tâches que nous proposons : tout le monde est bienvenu !

### Tâches

**1. Résumé automatique de commentaires**

*Objectifs*

Dans le cadre de la promotion de produits sur les plateformes en ligne, l’appréciation peut être analysée à partir des retours utilisateurs (User Generated Content). Ces derniers peuvent se présenter : notes, étoiles, mais aussi avis et commentaires textuels. Les notes n’étant pas toujours en adéquation avec les contenus textuels, de plus en plus d’acteurs cherchent à qualifier l’opinion des utilisateurs et à déterminer quels sont leurs arguments.

La thématique est orientée sur les avis et commentaires concernant l’offre de logements en région centre (particuliers, auberges, hôtels, luxe, etc.). Il s’agira de construire un résumé automatique des commentaires, à partir des arguments détectés dans ces derniers, à comparer aux notes et/ou à la description. Ce résumé orienté devra être séparé en deux champs principaux : points positifs et points négatifs sur des critères communs : accueil, confort, services, propreté, accessibilité, etc. D’autres champs peuvent être proposés par les participants selon les arguments extraits à partir des commentaires.

*Sous tâches*

- Traitement / débruitage de données UGC
- Détection et extraction d’arguments
- Agrégation des valeurs par produits
- Détection et résolution de contradictions
- Résumé automatique d’opinions sur les aspects

*Données et évaluation*

Collection de données représentant chaque produit en ligne (champs de description du produit, notes ou étoiles, liste des commentaires associés) en français et en anglais. Les données seront fournies sous-forme de corpus (pour le corpus collecté sur Internet) et/ou via des liens à télécharger (pour les données fournies par les partenaires, à préciser).

L’évaluation portera sur la capacité à calculer automatiquement les scores pour chaque catégorie d’évaluation du produit (accueil, propreté, emplacement, etc.). Pour chacun de ces scores, un argumentaire résumé automatiquement devra être fourni qui pourra faire l’objet d’évaluation qualitatives.

**2. Identification des tendances stratégiques liées aux brevets**

*Objectifs*

La stratégie de dépôt de brevets par des entreprises ou des individus représente un enjeu considérable, qui a donné lieu à des affaires mondialement connues (Apple vs Samsung, Microsoft vs Google). Cet outil juridique reste cependant difficilement accessible pour les entreprises de petite taille ou les individus. En particulier, il n’est pas évident de déterminer quelles technologies vont avoir tendance à être l’objet de brevets, dans une optique de veille ou de préservation de la propriété intellectuelle.

La tâche proposée vise à mieux modéliser les mécanismes qui permettent de prédire l’apparition de brevets pour des technologies en essor, par utilisation de méthodes d’IA et de TAL (terminologie et expressions multi-mots, catégorisation des brevets, évolution des termes et des n-grams, prédiction de tendances). L’objectif est de déterminer, au regard des données collectées sur des brevets (par ex. distribution des termes entre 2001 et 2009), quels brevets seront déposés (par ex. en 2010). Pour illustration : si "tactile" est recensé avec une grande montée en 2010, pouvait-on prédire cette montée en exploitant les données de la décennie précédente ?

*Sous tâches*

- Prétraitement du langage et de la structure des brevets
- Extraction de terminologies liées aux technologies
- Comparaison des termes des brevets avec les sites technologiques
- Détection de signaux faibles
- Analyse et prédiction de tendances

*Données et évaluation*

Seront mis à disposition :

- Brevets de classes A/G/H en français 2001 - 2016 (descriptions, revendications)
- Google n-gram du français
- Corpus de sites technologiques (aspirés et nettoyés)

Deux évaluations seront proposées :

- Quantitative : quel système prédit le mieux la liste conjointe de tous les termes établie par les différents groupes qui participe à la tâche ?
- Qualitative : quel système d'interrogation et de visualisation des données est le plus pertinent et le plus ergonomique ?


### Planning prévisionnel

Samedi 24 juin (Lab’O)

- 14h-15h : présentation du hackathon, café
- 15h-16h : échanges, constitution des équipes, précisions sur les objectifs
- 16h-20h : développements en équipes
- 20h-21h : pause repas
- 21h-... : développements en équipes

Dimanche 25 juin (Lab’O)

- 09h-10h : accueil, café
- 10h-12h : développements en équipes
- 12h-13h : pause repas
- 13h-14h : présentation des premiers résultats
- 14h-19h : développements en équipes

Lundi 26 juin (à TALN sur Orléans)

- 14h-17h : présentation des résultats, discussions, remise du prix

### Organisation pratique

BYOD (amenez votre ordinateur)  
Pas de critères pour participer, HackaTAL est ouvert à tous !  
Aucune préparation n’est requise de la part des participants en amont de l’évènement  
Données et briques logicielles seront en ligne : https://github.com/HackaTAL/2017  

### Organisateurs

Julien Borderieux (LLL)  
Victor Brandao (Lab’O)  
Patrice Frutos (INPI)  
Kim Gerdes (Paris 3, Cloem.com)  
Loïc Grobol (LaTTiCe)  
Gaël Guibon (LSIS, Caléa Solutions)  
Anaïs Lefeuvre-Halftermeyer (LIFO)  
Pierre-Edouard Lieb (Recast.AI)  
Gilles Mary (Lab’O)  
Djamel Mostefa (SYSTRAN)  
Gilles Moyse (Récital)  
Damien Nouvel (ERTIM)  
Namrata Patel (Viseo)  
Paul Renvoise (Recast.AI)  
