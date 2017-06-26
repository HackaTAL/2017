#!/usr/bin/python3
import sqlite3, os, re, nltk, ast
from data2dict import wordListToFreqDict, fichiermakeDict, filtreDico, tokenizeValues, descRev2tok, evalTexte

"""
Auteurs : Marine Courtin & Arthur Provenier
Création d'une base de données à partir des fichiers textes fournis
À lancer au même niveau que le dossier "hasIpcCorr" et que data2dict.py
Si la base de données existe déjà, il faut la supprimer puis relancer (très opti)
"""

conn = sqlite3.connect('database.db')

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS fichiers(
     nom_fichier TEXT PRIMARY KEY UNIQUE,
     date TEXT KEY,
     domaine1 TEXT NOT NULL DEFAULT '',
     domaine2 TEXT NOT NULL DEFAULT '',
     domaine3 TEXT NOT NULL DEFAULT ''
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS mega_table(
     n_fich TEXT KEY,
     token TEXT KEY,
     freq_d INTEGER NOT NULL DEFAULT 0,
     freq_r INTEGER NOT NULL DEFAULT 0
)
""")
conn.commit()

dossier = "hasIpcCorr"
for root, dirs, files in os.walk(dossier, topdown=False):
	for name in files:
		print (name)
		complete_path = os.path.join(root, name)
		test = evalTexte(open(complete_path).read())
		if test:
			dico = filtreDico(fichiermakeDict(complete_path))
			new_dico = tokenizeValues(dico)
			DIC = descRev2tok(new_dico)
			cursor.execute("""INSERT INTO fichiers(nom_fichier, date, domaine1, domaine2, domaine3) VALUES(?, ?, ?, ?, ?)""", [DIC["fichier"], DIC["annee"], DIC["domaine1"], DIC["domaine2"], DIC["domaine3"]])
			conn.commit()
			for t in DIC["tokens"]:
				cursor.execute("""INSERT INTO mega_table(n_fich, token, freq_d, freq_r) VALUES(?, ?, ?, ?)""", [DIC["fichier"],t, DIC["tokens"][t][0], DIC["tokens"][t][1]])
				conn.commit()

conn.close()

