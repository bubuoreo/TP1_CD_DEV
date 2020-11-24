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


def nbJours(year,month):
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
        return ("Le mois", m, "de l'année", y, "est un mois de 30 jours")
    elif m in liste31 :
        return ("Le mois", m, "de l'année", y, "est un mois de 31 jours")
    elif m == 2 :
        if bisextile == True :
            return ("Ce mois de Février de l'année", y, "est un mois de 29 jours")
        else :
            return ("Ce mois de Février de l'année", y, "est un mois de 28 jours")
