# Participants

- Arthur
- Marine

# Description

Les scripts et la base de données suivants ont été constitués par Arthur et Marine au cours du hackaTAL 2017.

+ **data2dict.py** : Les fonctions incluses dans ce script permettent de créer les dictionnaires que l'on utilisera afin de construire la base de données. Ces dictionnaires contiennent des informations relatives à l'année, les domaines, le nom du fichier, ainsi qu'à la fréquence des tokens dans la description et dans les revendications pour chaque brevet de l'arborescence.

+ **creation_db.py** : Ce script permet de créer une base de données contenant deux tables que l'on pourra interroger par la suite à l'aide de requêtes SQL.

+ **interrogation.py** : Ce dernier script permet d'interroger la base de données et de visualiser les résultats de la requête. Deux paramétrages sont possibles : choix du token en ligne de commande (dans ce cas on visualisera la fréquence absolue du token dans les descriptions et les revendications en fonction de l'année de publication du brevet), ou encore modification plus précise de la requête SQL à l'intérieur du script lui-même. On obtient alors le graphiques correspondant aux résultats de la requête.

+ **database.db** : Cette base de données à été constituée à partir d'échantillons des brevets fournis (le temps de traitement étant trop long pour nous permettre d'appliquer nos scripts à l'ensemble des données). Cependant, il est tout à fait possible de créer la base de données complète en utilisant les scripts fournis.


Pistes que nous aurions souhaité explorer:

- intégrer les sous-domaines à la base de données
- utiliser des fréquences relatives plutôt qu'absolues
- construire une courbe représentant les variations de fréquences associées à un terme qui devient populaire dans les brevets, dans le but de trouver les tokens dont la courbe de fréquence semble suivre le même motif (-> prédiction)
- tester les fréquences de bigrammes
- rendre la visualisation interactive (dropdown menu pour sélectionner le domaine, le sous-domaine; menu permettant d'entrer le token souhaité)
