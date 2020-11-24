# Burlot Alexandre
# 24/11/2020
# TODO: 
# - Ecrire une fonction qui renvoie un bool disant si l'année renseignée est bisextile ou pas 
# - Écrire une fonction qui donne le nombre de jours d'un mois après avoir vérifié la validité des
# paramètres.
# - Écrire une fonction qui vérifiera si une date est valide ou pas (True signifie date valide, False sinon)
# - Écrire le programme principal qui propose la saisie d'une date, la valide et affiche le message "date
# valide" ou "date non valide" selon le cas

def checkBisextile(year): 
# Fonction qui vérifie si l'année choisi est bisextile selon les critère demandés dans l'énoncé
    try:
        y = int(year)
    except Exception as ex:
        return (ex, ": Vous n'avez pas rentré une année, merci de réitérer l'opération en inscrivant une année dans la fonction")
    if y % 400 == 0:
        return (True)
    elif y % 100 != 0 and y % 4 == 0 :
        return (True)
    else :
        return (False)


def nbJours(month,year):
    # Fonction qui donne le nombre de jours dans le mois en fonction de l'année
    
    bisextile = None
    liste31 = [1,3,5,7,8,10,12]
    liste30 = [4,6,9,11]

    try:
        y = int(year)
        m = int(month)
    except Exception as ex:
        return (ex, ": les paramètres rentrés ne sont pas corrects,"
        "assurez vous que le mois est compris entre 1 et 12 et que l'année comporte 4 chiffres")

    if checkBisextile(y) == True :
        bisextile = True
    else :
        bisextile = False

    if m in liste30 :
        return (30, "Ce mois contient 30 jours")
    elif m in liste31 :
        return (31, "Ce mois contient 31 jours")
    elif m == 2 :
        if bisextile == True :
            return (29, "Ce mois de Février est un mois de 29 jours")
        else :
            return (28, "Ce mois de Février est un mois de 28 jours")
    else : 
        return ("le mois entré n'est pas un nombre entre 1 et 12")


def dateValidation(day,month,year):
    # Fonction nous retournant la validité d'une date entrée

    try:
        
        y = int(year)
        m = int(month)
        d = int(day)
        d >= 1
        m >= 1
        m <= 12
    except Exception as ex:
        return (ex, ": Date non valide")
    lastday = nbJours(m,y)[0]
    if d <= lastday :
        return ("Date valide")
    else :
        return ("Date non valide")
    
