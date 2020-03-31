from Fonctions.fonctions import *

# Courbe de Gosper
dessiner(axiome=iterer(axiome="A", quantite=saisir("Nombre d'itérations(s) : ", "entier"), signes=["+", "-"], lettres={"A":"A-B--B+A++AA+B-", "B":"+A-BB--B-A++A+B"}), longueur=saisir("Longueur d'un segment : ", "entier"), vitesse=0, couleur=saisir("Couleur : ", "texte"), position=[(-250, 0), 90], angle=60, unique=True, lettres=["A", "B"])