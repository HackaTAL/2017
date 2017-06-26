import os, re, ast


def wordListToFreqDict(wordlist):
    """
    input : liste de tokens
    output : dico {token : freq}
    """
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))

def fichiermakeDict(fichier):
    """
    input : nom de fichier
    output : dico {description : "blabla", revendication : "bla", domaines : []}
    """
    dico={}
    nom_fichier = fichier.split("/")[-1]
    dico['fichier']=nom_fichier
    texte = open(fichier).read()
    motif = re.compile("(.+?) ::: (.+?)\n\n?")
    values = re.findall(motif, texte)
    for value in values:
        if value:
            key = value[0]
            if key not in dico:
                if key != 'ipc':
                    valeur = value[1]
                else: valeur = [value[1]]
            else:
                valeur += [value[1]]
            if valeur:
                dico[key]=valeur
    return dico


def filtreDico(dico):
    """
    input : le dictionnaire retourné par fichiermakeDict
    output : un dictionnaire filtre avec comme cles la description, revendication, domaine, annee
    """
    sous_dico = {}
    sous_dico['annee'] = dico.get('date')[:4]
    sous_dico['fichier'] = dico.get('fichier')
    sous_dico['revendication'] = dico.get('claims')
    sous_dico['description'] = dico.get('description')
    sous_dico['domaine1'] = "null"
    sous_dico['domaine2'] = "null"
    sous_dico['domaine3'] = "null"
    count = 1
    vus =[]
    for elt in dico.get('ipc'):
        if elt[0] == "A" or elt[0] =="G" or elt[0]=="H":
            if elt[0] in vus:
                continue
            sous_dico['domaine'+str(count)] = elt[0]
            vus+=elt[0]
            count+=1
    return sous_dico


def tokenizeValues(dico):
    """
    input : le dico retourne par filtreDico
    output : {description : {token:freq}, revendications : {token:freq}, annee : "", domaine : []}
    ! les textes sont normalisés -> lowercase avant tokenisation / comptage
    """
    nouveau_dico = {}
    for key in dico:
        # print(key)
        if key ==  'description' or key== 'revendication':
            old_value = dico.get(key).lower()
            valeur = wordListToFreqDict(re.split("\W+", old_value))
        else:
            valeur = dico.get(key)
        nouveau_dico[key] = valeur
    return nouveau_dico

def descRev2tok(dico):
    """
    input : le dico retourne par tokenizeValues
    output : {fichier:, date:, token:[freqDesc, freqRev]}
    """
    nouveau_dico = {}
    all_dict = [dico['revendication'], dico['description']]
    all_key = set().union(*all_dict)
    nouveau_dico['tokens'] ={}
    for key in dico:
        if key != 'revendication' or key != 'description':
            nouveau_dico[key]=dico.get(key)
    for token in all_key:
        nouveau_dico['tokens'][token]= [dico['description'].get(token, 0), dico['revendication'].get(token, 0)]
    nouveau_dico_2={key:nouveau_dico[key] for key in nouveau_dico if key != 'revendication' and key != 'description'}
    return nouveau_dico_2

def evalTexte(texte):
    """
    input : texte
    output : True si le fichier respecte bon format, false otherwise
    """
    test1 = re.search("claims :::", texte)
    test2 = re.search("date :::", texte)
    test3 = re.search("ipc :::", texte)
    test4 = re.search("description :::", texte)
    if test1 is not None and test2 is not None and test3 is not None and test4 is not None:
        result = True
    else:
        result = False
    return result

def dossier2ListDict(dossier):
    """
    input : name of dir containing the data (may have subdir)
    output : list where each element is a dictionary {
    fichier :
    annee :
    domaine1 :
    tokens {token : [freqdescription, freqRevendication]}
    }
    """
    listeDicoGlobale = []
    for root, dirs, files in os.walk(dossier, topdown=False):
        for name in files:
            # print(name, "\n\n")
            complete_path = os.path.join(root, name)
            test = evalTexte(open(complete_path).read())
            if test == False:
                continue
            dico = filtreDico(fichiermakeDict(complete_path))
            new_dico = tokenizeValues(dico)
            listeDicoGlobale.append(new_dico)
    return listeDicoGlobale


#### Lancement du traitement
