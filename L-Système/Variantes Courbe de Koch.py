from Fonctions.fonctions import *

# Variantes Courbe de Koch
choix = choix(3, "Type de courbe de Koch :~~#0766ea||Sans point double~~black~~grey||Croix en « + »~~black~~grey||Croix à 45°~~black~~grey")

# Sans point double
if choix == 1:
	dessiner(iterer("A", saisir("Nombre d'itérations(s) : ", "entier"), ["+", "-"], {"A":"A+B-A-B+A", "B":"B-A+B+A-B"}), saisir("Longueur d'un segment : ", "entier"), 0, saisir("Couleur : ", "texte"), [(-750, -400), 0], 90, True, ["A", "B"])
# Croix en « + »
elif choix == 2:
	dessiner(iterer("F+F+F+F", saisir("Nombre d'itérations(s) : ", "entier"), ["+", "-"], {"F":"F+F-F-F+F"}), saisir("Longueur d'un segment : ", "entier"), 0, saisir("Couleur : ", "texte"), [(-750, 0), -45], 90, True, ["F"])
# Croix à 45°
elif choix == 3:
	dessiner(iterer("F+F+F+F", saisir("Nombre d'itérations(s) : ", "entier"), ["+", "-"], {"F":"F+F-F-F+F"}), saisir("Longueur d'un segment : ", "entier"), 0, saisir("Couleur : ", "texte"), [(-750, -400), 0], 90, True, ["F"])