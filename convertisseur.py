##### CONVERTISSEUR UNIVERSEL ######

#Liste de tuple qui associe le préfixr à la puissance de 10 correspondante
multiple = [
    (-12, "p"),
    (-9, "n"),
    (-6, "u"),
    (-3, "m"),
    (-2, "c"),
    (-1, "d"),
    (1, "da"),
    (2, "h"),
    (3, "k"),
    (6, "M"),
    (9, "G"),
    (12, "T"),
]


#Choix de l'utilisateur. Continuer ou arrêter.
def menu():
    print("Que voulez-vous faire ?")
    print("1/ Convertir une mesure dans une sous-unité ou un multiple")
    print("2/ Sortir du programme")
    chx = input("Votre choix :")
    while (chx != "1") and (chx != "2"):
        print("Choix invalide !")
        chx = input("Votre choix :")
    return int(chx)

#renvoie le dernier element d'une chaine de caractère "mA" --> "A"
def dernier_element(string):
    return string[len(string)-1 : len(string)]

#renvoie le premier element d'une chaine de caractère "mA" --> "m"
def premier_element(string):
    return string[0:1]

#Entrée des valeurs à convertir. On verifie l'homogénéité des unités
def entree_valeurs():
    val = float(input("Quelle est la valeur à convertir (sans l'unité)?"))
    unite = input("Quelle est son unité ?")
    sous_unite = input("Vers  quelle unité voulez-vous la convertir ?")
    while dernier_element(unite) != dernier_element(sous_unite):
        print("CONVERSION IMPOSSIBLE - DONNEES NON HOMOGENES")
        unite = input("Quelle est son unité ?")
        sous_unite = input("Vers  quelle unité voulez-vous la convertir ?")
    return (val, unite, sous_unite)

#Va chercher dans la liste multiple la puissance de 10 correspondant au prefixe
def quel_multiple(prefixe):
    for m in multiple:
        if m[1] == prefixe:
            return m[0]

#Convertit la valeur dans l'unité demandée
def convertisseur(val, unite, sous_unite):
    #Test pour s'assurer que la donnée n'est pas dans l'unité (la chaine a une longueur de 1)
    if len(unite)==1:
        multiple_init = 0
    else:
        multiple_init = quel_multiple(premier_element(unite))
    if len(sous_unite)==1:
        multiple_fin = 0
    else:
        multiple_fin = quel_multiple(premier_element(sous_unite))
    puissance = multiple_init - multiple_fin
    #Mise en forme du résultat. La conversion en float se charge de faire le travail
    valeur_convertie = float(str(val) + "e" + str(puissance))
    return valeur_convertie

# affiche le résultat
def affiche(valeur_convertie,unite_finale):
    print("Valeur convertie :",str(valeur_convertie)+" "+unite_finale)
    print("")
    
    
#fonction main, lancée en début de programme.
def main():
    while menu() != 2:
        val, u, sous_u = entree_valeurs()
        val_conv = convertisseur(val, u, sous_u)
        affiche(val_conv,sous_u)


if __name__ == "__main__":
    main()
