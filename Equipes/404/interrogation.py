#!/usr/bin/python3
# usage : python3 interrogation.py token
import sys
import sqlite3
import numpy as np
import matplotlib.pyplot as plt

"""
Auteurs : Marine Courtin & Arthur Provenier
Interface pour interroger la base de données créée par creation_db.py
À partir d'un token, retourne un graphique avec
	en abscisse les années
	en ordonnée la fréquence du token dans les revenditions et dans les descriptions
Possibilité de modifier la requête pour convenir à son utilisation ...
"""


conn = sqlite3.connect('database.db')
c = conn.cursor()

# Le mot que l'on cherche (peut-être adapté comme argument en ligne de commande)
wordUsed = str(sys.argv[1])

# La requête
sql = 'select date, token, sum(freq_r), sum(freq_d) from mega_table INNER JOIN fichiers ON mega_table.n_fich = fichiers.nom_fichier where token=? GROUP BY (date)'


y1 = [] # La fréquence dans les revendications
y2 = [] # La fréquence pour les tokens dans la description
names = [] # Nom du fichier ou années ... forcément un string ?
# Extrait chaque row de la requête retournée
for row in c.execute(sql, [(wordUsed)]):
    startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
    splitInfo = startingInfo.split(',')
    names.append(splitInfo[0])
    y1.append(splitInfo[2])
    y2.append(splitInfo[3])
y1 = np.array(y1) # Transforme en array de numpy
y2 = np.array(y2) # idem

# Utile pour afficher les strings en abscisse
x = np.arange(len(names))
plt.xticks(x, names)

# Création du plot ...
plt.plot(x, y1, label='freq_r')
plt.plot( x, y2, label='freq_d')

# Légende des axes
plt.xlabel('Date')
plt.ylabel('Fréquence')
plt.legend()

plt.show()

conn.close()
