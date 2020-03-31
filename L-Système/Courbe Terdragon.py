from Fonctions.fonctions import *

# Courbe Terdragon
dessiner(axiome=iterer(axiome="F", quantite=saisir("Nombre d'itérations(s) : ", "entier"), signes=["+", "-"], lettres={"F":"F+F-F"}), longueur=saisir("Longueur d'un segment : ", "entier"), vitesse=0, couleur=saisir("Couleur : ", "texte"), position=[(50, -250), 225], angle=120, unique=True, lettres=["F"])