from Fonctions.fonctions import *

# Courbe de Koch
dessiner(iterer("F", saisir("Nombre d'itérations(s) : ", "entier"), ["+", "-"], {"F":"F+F-F-F+F"}), saisir("Longueur d'un segment : ", "entier"), 0, saisir("Couleur : ", "texte"), [(-250, -100), 0], 90, True, ["F"])