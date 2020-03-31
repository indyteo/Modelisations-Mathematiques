from Fonctions.fonctions import *

# Triple Flocon de Koch
dessiner(axiome=iterer(axiome="F--F--F", quantite=saisir("Nombre d'itérations(s) : ", "entier")), longueur=saisir("Longueur d'un segment : ", "entier"), couleur=saisir("Couleur : ", "texte"), position=[(-300, 150), 0])