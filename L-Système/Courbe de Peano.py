from Fonctions.fonctions import *

# Courbe de Peano
dessiner(iterer("L", saisir("Nombre d'itérations(s) : ", "entier"), ["+", "-", "F"], {"L":"LFRFL-F-RFLFR+F+LFRFL", "R":"RFLFR+F+LFRFL-F-RFLFR"}), saisir("Longueur d'un segment : ", "entier"), 0, saisir("Couleur : ", "texte"), [(-250, -100), 90], 90, True, ["F"])