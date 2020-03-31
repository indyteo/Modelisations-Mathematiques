from Fonctions.fonctions import *

# Triple Flocon de Koch
Nb = saisir("Nombre d'itérations(s) : ", "entier")
Longueur = saisir("Longueur d'un segment : ", "entier")
Couleur = saisir("Couleur : ", "texte")
dessiner(axiome=iterer(axiome="F--F--F", quantite=0), longueur=Longueur, couleur=Couleur, position=[(-300, 150), 0], unique=False)
for i in range(Nb):
	dessiner(axiome=iterer(axiome="F--F--F", quantite=i+1), longueur=Longueur/(3**(i+1)), couleur=Couleur, position=[(-300, 150), 0], unique=False)
turtle.mainloop()