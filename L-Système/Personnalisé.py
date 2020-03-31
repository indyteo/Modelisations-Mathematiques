from Fonctions.fonctions import *

# Personnalisé
Axiome = saisir("Axiome de départ : ")
Signes = saisir("Caractères qui ne sont pas transformés.||Caractère n°{numero} : ||texte", "liste")
Lettres = saisir("Définition du L-Système.||Caractère à remplacer n°{numero} : ||Caractère(s) de remplacement de {cle} (n°{numero}) : ||texte", "dictionnaire")
Angle = saisir("Angle : ", "entier")
Avancer = saisir("Caractères signifiant \"Avancer\".||Caractère n°{numero} : ||texte", "liste")
Position = [saisir("Position de départ (x, y).||Position n°{numero} : ||entier", "tuple"), saisir("Inclinaison de départ (0 = Droite, 90 = Haut, 180 = Gauche, 270 = Bas) : ", "entier")]
dessiner(axiome=iterer(axiome=Axiome, quantite=saisir("Nombre d'itérations(s) : ", "entier"), signes=Signes, lettres=Lettres), longueur=saisir("Longueur d'un segment : ", "entier"), vitesse=0, couleur=saisir("Couleur : ", "texte"), position=Position, angle=Angle, unique=True, lettres=Avancer)