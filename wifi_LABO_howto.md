Se connecter au wifi du LAB'O
=============================

  1. Aller à `https://10.250.1.10/guest/LAB0.php?_browser=1`. Ajouter une exception de sécurité si nécéssaire
  2. Entrer vos identifiants de connexion (dispo sur la table à l'entrée)
  3. Vous êtes redirigé sur `securelogin.arubanetworks.com`. Si cela déclenche une alerte de sécurité, ajouter également une exception
    - Si la redirection foire
      - Sous Linux, ajouter à `/etc/hosts/` une ligne contenant `172.31.98.1     securelogin.arubanetworks.com` et reprenez au point 1.

Si ça ne marche toujours pas, allez voir Loïc et voyez ça ensemble.
