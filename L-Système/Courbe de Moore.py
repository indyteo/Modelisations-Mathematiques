from Fonctions.fonctions import *

# Courbe de Moore
dessiner(iterer("LFL+F+LFL", saisir("Nombre d'itérations(s) : ", "entier"), ["+", "-", "F"], {"L":"-RF+LFL+FR-", "R":"+LF-RFR-FL+"}), saisir("Longueur d'un segment : ", "entier"), 0, saisir("Couleur : ", "texte"), [(0, -100), 90], 90, True, ["F"])