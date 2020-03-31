from Fonctions.fonctions import *

# Triangle de Sierpinski
Nb = saisir("Nombre d'itérations(s) : ", "entier")
Triangle = iterer("X", Nb, ["+", "-"], {"F":"FF", "X":"--FXF++FXF++FXF--"})

for i in range(6*(2**Nb)):
	Triangle += "F"
	if i+1 == 2**Nb or i+1 == 3*(2**Nb) or i+1 == 5*(2**Nb):
		Triangle += "--"

dessiner(Triangle, saisir("Longueur d'un segment : ", "entier"), 0, saisir("Couleur : ", "texte"), [(0, 0), 180], 60, True, ["F"])