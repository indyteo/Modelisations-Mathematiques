from Fonctions.fonctions import *

# Courbe du dragon
dessiner(axiome=iterer(axiome="FX", quantite=saisir("Nombre d'itérations(s) : ", "entier"), signes=["+", "-"], lettres={"X":"X+YF+", "Y":"-FX-Y"}), longueur=saisir("Longueur d'un segment : ", "entier"), vitesse=0, couleur=saisir("Couleur : ", "texte"), position=[(-250, 0), 225], angle=90, unique=True, lettres=["F"])