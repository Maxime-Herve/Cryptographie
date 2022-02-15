import random
import string

# Carré de polybe qui nous servira pour les fonctions suivantes
carre_de_polybe = [['A','B','C','D','E'],
                   ['F','G','H','I','J'],
                   ['K','L','M','N','O'],
                   ['P','Q','R','S','T'],
                   ['U','V','X','Y','Z']]

def Cesar_lettre (lettre,cle) :
    #Vérification si la lettre entrée est bien une lettre
    if(ord(lettre.upper())>64 and ord(lettre.upper()) <91):
        #on calcul la lettre qu'on obtient avec la cle
        lettre = chr(((ord(lettre.upper()) - 65) + cle)%26 + 65)
    return lettre
   
    
def Cesar (texte,cle) :
    L = ""
    #Parcour de chaque lettre du texte
    for i in range(len(texte)) :
        #Pour chaque lettre on la modifie en fonction de la clee
        L = L + Cesar_lettre (texte[i],cle)
    return L

def Decode_Cesar (texte,cle):
    res = "Erreur"
    #Pour décoder il suffit de recoder avec l'opposé de la cle
    if(texte.isupper()):
        res = Cesar(texte,-cle)
        
    return res


def Decode_Cesar_v2 (texte) :
    L=[0,'a']
    res=""
    # Parcour des 26 lettres
    for i in range(26):
        #On compte le nombre de fois que la lettre apparait dans le texte
        NbOcc=texte.count(string.ascii_uppercase[i])
        #Si la lettre apparait plus de fois que celle qu'on a le plus rencontrée
        if(NbOcc>L[0]):
            #On enregistre la lettre qui apparait le plus de fois dans la liste
            L[1]=string.ascii_uppercase[i]
            #Le nombre de fois que cette lettre apparait
            L[0]=NbOcc
    #On calcule la clee en regardant le decalage de cette lettre 
    #par rapport au e qui est souvent la lettre la plus utilisée
    clee=ord('E')-ord(L[1])
    #On décode le texte avec la clee trouvé
    res="clée : "+str(clee)+" texte : "+Cesar(texte, clee)
    return res
    

def alphabet_substitution () : 
    res = ""
    temp = ""
    txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26) :
        #Choix aléatoirr afin de remplacer une des lettre
        temp = random.choice(txt)
        res += temp
        #permet de supprimer la lettre qui a été utilisée
        txt = txt.replace(temp, '')
    return res

def Code_subst (texte,alphabet) : 
    #On met le texte et l'alphabet en majuscule
    texte = texte.upper()
    alphabet = alphabet.upper()
    res = ""
    #Parcour de tout le texte
    for i in range(len(texte)) :
        #permet de selectionner uniquement les majuscule, dans notre
        #cas c'est pour ne pas avoir les caractère autre que les lettres
        if(texte[i].isupper()) :
            #codeage de la lettre
            res += alphabet[ord(texte[i]) - 65]
        else :
            res += texte[i]
    return res

def Decode_subst (texte,alphabet) : 
    res = ""
    #parcour de tout le texte
    for i in range(len(texte)) :
        #si c'est une majuscule on la décode sinon non
        if(texte[i].isupper()) :
            res += chr(str.find(alphabet, texte[i]) + 65)
        else :
            res += texte[i]
    return res


# Fonction qui créer une table de Vigenère
def Table_Vigenere () -> str: 
    
    # Déclaration des variables
    res = []
    temp = ""  
    
    # Pour les 25 décalage de l'alphabet
    for i in range(26) :
    
        # Pour les 26 lettres de l'alphabet
        for j in range(26) :
            
            # On ajoute à l'alphabet temporaire un alphabet avec un décalage j
            temp += chr((j + i)%26 + 65)
        
        # On ajoute le nouveau décalage à notre table
        res.append(temp)
        
        # On vide l'alphabet temporaire
        temp = ""
    
    return res

# Fonction qui code en utilisant le système de Vigenère
def Code_Vigenere (texte : str,cle : str,table : str) -> str: 
    
    # Déclaration des variables
    resultat = ""
    
    # On met le texte et la clé en majuscule et on enlève les espaces
    texte = texte.upper()
    texte = texte.replace(' ', '')
    cle = cle.upper()
    cle = cle.replace(' ', '')
    
    # Pour chaque caractères du texte
    for i in range(len(texte)) :
        
        # On récupère le code ASCII du caratère du texte et de la clé 
        # qu'on ramène dans l'intervalle [0,25]
        # On traduit ses index par une lettre dans la table[x,y]
        # x = index du caractère texte[i] dans l'alphabet
        # y = index du caractère cle[i % taille clé] dans l'alphabet
        # On ajoute le caractère obtenu au résultat
        resultat += table[ord(texte[i]) - 65][ord(cle[i%len(cle)]) - 65]
    
    return resultat
    
# Fonction qui décode en utilisant le système de Vigenère    
def Decode_Vigenere (texte : str,cle : str,table : str) -> str: 
    
    # Déclaration des variables
    resultat = ""
    index = 0
    
    # On met le texte et la clé en majuscule et on enlève les espaces
    texte = texte.upper()
    texte = texte.replace(' ', '')
    cle = cle.upper()
    cle = cle.replace(' ', '')
    
    # Pour chaque caractères du texte
    for i in range(len(texte)) :
        
        # Pour la colonne à l'index du caractère de la clé :
        # Si le caractère séléctionné dans la table est égal au caractère dans le texte
        # Alors on sort de la boucle
        # Sinon, on incrément et on passe au prochain index
        while(table[index][ord(cle[i%len(cle)]) - 65] != texte[i]) :
            
            # On incrémente la variable
            index += 1
        
        # On ajoute le caractère trouvé
        resultat += chr(index + 65)
        
        # On réinitialise l'index
        index = 0
        
    return resultat  


# Fonction qui code en utilisant le carré de polybe 
def Code_Polybe_v1 (texte : str) -> list : 
    
    # Déclaration des variables
    resultat = []
    ligne = 0
    colonne = 0
    
    # On met le texte en majuscule et on enlève les espace
    # On transforme les W  en V
    texte = texte.upper()
    texte = texte.replace(' ', '')
    texte = texte.replace('W', 'V')

    # Pour chaque caractères du texte
    for i in range(len(texte)) :
        
        # Si le caractère qu'on recherche n'est pas égal à une case dans le carré
        while (carre_de_polybe[ligne][colonne] != texte[i]) :
            
            # On incrémente la variable
            colonne += 1
            
            # Si la colonne "sort" du carré, est la remet à 0 et on change de ligne
            if(colonne == 5) :
                colonne = 0
                ligne += 1
                
        # On ajoute les index (+1 car l'index de la table commence à 1 et non 0) au résulat 
        resultat.append(int(str(ligne + 1) + str(colonne + 1)))
        
        # On réinitialise les index
        ligne = 0
        colonne = 0
                
    return resultat


# Fonction qui décode en utilisant le carré de polybe 
def Decode_Polybe_v1 (texte : list) -> str : 
    
    # Déclaration des variables
    res = ""
    
    # Pour chaque caractères du texte
    for i in range (len(texte)) :
        
        # On récupère le caractère correspondant dans la table de polybe
        res += carre_de_polybe[int(str(texte[i])[0]) - 1][int(str(texte[i])[1]) - 1]
        
    return res


# Fonction qui génère un carré de polybe "amélioré" grâce à une clé
def Tableau_Polybe (cle : str) -> list:
    
    # Déclaration des variables
    cle_temporaire = ""
    index = 0
    ligne = 0
    res = [[],[],[],[],[]]
    
    # On met la clé en majuscule et on enlève les espace
    cle = cle.upper()
    cle = cle.replace(' ', '')
    
    
    # Boucle qui permet d'enlever les doublons
    # Pour chaque caractères dans la clé
    for caractere in cle:
        
        # Si le caractere n'est pas présent dans la clé temporaire
        if caractere not in cle_temporaire:
            
            # On l'ajoute
            cle_temporaire += caractere
    
    # Clé sans doublons
    cle = cle_temporaire
    
    # Pour chaque caractères dans la clé
    for index in range(len(cle)) :
        
        # Si la colonne "sort" du carré, on change de ligne
        if(index%5 == 0 and index != 0) :
            ligne = ligne + 1
            
        # On ajoute le caractère au carré de polybe
        res[ligne].append(ord(cle[index]) - 65)
       
    # On increment index pour la suite
    index += 1
    
    # Si la colonne "sort" du carré, on change de ligne
    if(index%5 == 0 and index != 0) :
        ligne = ligne + 1
     
    # Boucle on l'on ajoute les lettres de l'alphabet manquant
    for lettre in range(26) :
        
        # On ne compte pas le W (pas dans le carré de polybe)
        if(lettre != 22) :
            
            # On vérifie que la lettre n'est pas déjà présente
            if(sum(x.count(lettre) for x in res) == 0) :
                
                # Ajoute la lettre non présent
                res[ligne].append(lettre)
                
                # Change d'index
                index += 1
                
                # Si la colonne "sort" du carré, on change de ligne
                if(index%5 == 0 and index != 0) :
                    ligne = ligne + 1
        
    return res


# Fonction qui code en utilisant le carré de polybe "amélioré" grâce à une clé
def Code_Polybe_v2 (texte : str, cle : str) -> list : 
    # Déclaration des variables
    resultat = []
    ligne = 0
    colonne = 0


    # On met la clé en majuscule et on enlève les espace
    cle = cle.upper()
    cle = cle.replace(' ', '')
    
    # On récupère un carré de polybe "amélioré" grâce à une clé
    cle = Tableau_Polybe(cle)
    
    # On met le texte en majuscule et on enlève les espace
    # On transforme les W  en V
    texte = texte.upper()
    texte = texte.replace(' ', '')
    texte = texte.replace('W', 'V')

    # Pour chaque caractères du texte
    for i in range(len(texte)) :
        
        # Si le caractère qu'on recherche n'est pas égal à une case dans le carré
        
        while (chr(cle[ligne][colonne] + 65) != texte[i]) :

            # On incrémente la variable
            colonne += 1
            
            # Si la colonne "sort" du carré, est la remet à 0 et on change de ligne
            if(colonne == 5) :
                colonne = 0
                ligne += 1
                
        # On ajoute les index (+1 car l'index de la table commence à 1 et non 0) au résulat 
        resultat.append(int(str(ligne + 1) + str(colonne + 1)))
        
        # On réinitialise les index
        ligne = 0
        colonne = 0
                
    return resultat


# Fonction qui décode en utilisant le carré de polybe "amélioré" grâce à une clé
def Decode_Polybe_v2 (liste : list, cle : str) -> str: 
    # Déclaration des variables
    res = ""

    # On met la clé en majuscule et on enlève les espace
    cle = cle.upper()
    cle = cle.replace(' ', '')
    
    # On récupère un carré de polybe "amélioré" grâce à une clé
    cle = Tableau_Polybe(cle)
    
    # Pour chaque caractères du texte
    for i in range (len(liste)) :

        # On récupère le caractère correspondant dans notre table de polybe amélioré
        res += chr(cle[int(str(liste[i])[0]) - 1][int(str(liste[i])[1]) - 1] + 65)
        
    return res


# Tests

"""
print("Cesar_lettre('a',3) : " + Cesar_lettre('a',3))
print("Cesar_lettre('Z',3) : " + Cesar_lettre('Z',3))
print("Cesar_lettre(' ',3) : " + Cesar_lettre(' ',3))
print("Cesar_lettre('>',3) : " + Cesar_lettre('>',3))
print("\n")

print("Cesar('abc WXY', 3) : " + Cesar('abc WXY', 3))
print("Decode_Cesar('DEF ZAB', 3) : " + Decode_Cesar('DEF ZAB', 3))
print("\n")

print( "Decode_Cesar_v2 n°1 : " + Decode_Cesar_v2("RM NIQA AWCDMVB KM ZMDM MBZIVOM MB XMVMBZIVB L'CVM NMUUM QVKWVVCM MB YCM R'IQUM MB YCQ U'IQUM MB YCQ V'MAB KPIYCM NWQA VQ BWCB I NIQB TI UMUM VQ BWCB I NIQB CVM ICBZM MB U'IQUM MB UM KWUXZMVL.»"))
print("\n")
print( "Decode_Cesar_v2 n°2 :: " + Decode_Cesar_v2("MZFAZ HAKX Z'MDDUHMUF BME À PADYUD. UX MXXGYM. EAZ VML YMDCGMUF YUZGUF HUZSF. UX BAGEEM GZ BDARAZP EAGBUD, E'MEEUF PMZE EAZ XUF, E'MBBGKMZF EGD EAZ BAXAOTAZ. UX BDUF GZ DAYMZ, UX X'AGHDUF, UX XGF; YMUE UX Z'K EMUEUEEMUF CG'GZ UYNDASXUA OAZRGE, UX NGFMUF À FAGF UZEFMZF EGD GZ YAF PAZF UX USZADMUF XM EUSZURUOMFUAZ. QJFDMUF PQ XM PUEBMDUFUAZ»"))
print("\n")

alphabet = alphabet_substitution()
print(alphabet)
print("\n")

print("Code_subst('AB cd:E', alphabet) : " + Code_subst('AB cd:E', alphabet))
print("\n")

print("Decode_subst(Code_subst('AB cd:E', alphabet) : " + Decode_subst(Code_subst('AB cd:E', alphabet), alphabet))
print("\n")

print(Table_Vigenere ())
print("\n")

print("Code_Vigenere('LE coDAGE', 'CRypTO', Table_Vigenere () : " + Code_Vigenere("LE coDAGE", "CRypTO", Table_Vigenere()))
print("\n")

print("Code_Polybe_v1 ('Spyware') : ")
print(Code_Polybe_v1 ("Spyware"))
print("\n")

print("Decode_Polybe_v1 (Code_Polybe_v1 ('Spyware')) : " + Decode_Polybe_v1(Code_Polybe_v1 ("Spyware")))
print("\n")

print("Tableau_Polybe('CRYptoGRAPHIE') : ")
print(Tableau_Polybe("CRYptoGRAPHIE"))
print("\n")

print("Code_Polybe_v2('SWITCHEZ', 'cryptoGRAphie') : ")
print(Code_Polybe_v2("SWITCHEZ", "cryptoGRAphie"))
print("\n")

print("Decode_Polybe_v2([51, 53, 25, 15, 11, 24, 31, 55], 'cryptoGRAphie') : " + Decode_Polybe_v2([51, 53, 25, 15, 11, 24, 31, 55], "cryptoGRAphie"))
print("\n")
"""