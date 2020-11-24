# Burlot Alexandre
# 24/11/2020
# TODO: 
# Ecrire une fonction qui renvoie un bool disant si l'année renseignée est bisextile ou pas 
#

def checkBisextile(year): 
# Fonction qui vérifie si l'année choisi est bisextile selon les critère demandés dans l'énoncé
    if year == int(year) :
        if int(year) == 0:
            return False
        if (int(year) % 400) == 0:
            return True
        elif str(year)[-2:] != '00' and int(year) % 4 == 0 :
            return True
        else :
            return False
    else :
        return ("Vous n'avez pas rentré une année, merci de réitérer l'opération en inscrivant une année dans la fonction")
