# Burlot Alexandre
# 24/11/2020
# TODO: 
# - Écrire une fonction qui teste si une année est bissextile ou non avec la convention suivante : la fonction
# renvoie la valeur True si l'année est bissextile, la valeur False dans le cas contraire.
# - Écrire une fonction qui donne le nombre de jours d'un mois après avoir vérifié la validité des
# paramètres.
# - Écrire une fonction qui vérifiera si une date est valide ou pas (True signifie date valide, False sinon)
# - Écrire le programme principal qui propose la saisie d'une date, la valide et affiche le message "date
# valide" ou "date non valide" selon le cas

import Calendar_func


print("Rentrez une date dans l'ordre jour/mois/année")
date = input("Allez y, rentrez votre date sous la forme demandée")
[day,month,year] = date.split("/")
print(Calendar_func.dateValidation(day,month,year))

print(Calendar_func.checkBisextile(-799))
print(Calendar_func.nbJours(4,2019)[1])
print(Calendar_func.dateValidation(29,2,2007))