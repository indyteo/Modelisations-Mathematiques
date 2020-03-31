import turtle
import colorsys
import tkinter

def choix(nb_choix=2, txt="Recommencer ?~~#0766ea||Oui~~green~~#c8f0c5||Non~~red~~#f2c0c0"):
	txt = txt.split("||")
	txt = [txt.split("~~") for txt in txt]
	fenetre = tkinter.Tk()
	tkinter.Label(fenetre, text=txt[0][0], fg=txt[0][1]).pack()
	var = tkinter.IntVar()
	for i in range(nb_choix):
		tkinter.Radiobutton(fenetre, text=txt[i+1][0], fg=txt[i+1][1], bg=txt[i+1][2], variable=var, value=i+1).pack(fill=tkinter.BOTH)
	tkinter.Button(fenetre, text="Valider", fg="green", bg="#c8f0c5", command=fenetre.quit).pack(fill=tkinter.BOTH)
	fenetre.mainloop()
	choix_utilisateur = var.get()
	try:
		fenetre.destroy()
	except:
		pass
	return choix_utilisateur

def saisir(txt=">>> ", type_var="texte"):
	"""
	Fonction demandant à l'utilisateur de saisir une variable d'un certain type.

	txt : Texte affiché dans le code "input(txt)"| Si type_var == "liste", vous devez écrire "Description de la liste||Élément n°{numero} : ||Type de variable souhaité dans la liste". | Si type_var == "tuple", vous devez écrire "Description du tuple||Élément n°{numero} : ||Type de variable souhaité dans le tuple". | Si type_var == "dico", vous devez écrire "Description du dictionnaire||Clé n°{numero} : ||Valeur n°{numero} (correspondant à {cle}) : ||Type de variable souhaité dans le dictionnaire". | Défaut = ">>> "
	type_var : Type de variable souhaité | Types valables : "texte", "entier", "decimal", "liste", "tuple" et "dictionnaire" | Défaut = "texte"
	"""

	try:
		if type_var == "texte":
			var = input(txt)
			if var == "":
				raise ValueError
		elif type_var == "entier":
			var = int(input(txt))
		elif type_var == "decimal":
			var = float(input(txt))
		elif type_var == "liste":
			var = []
			if txt == ">>> ":
				txt = "Aucune information sur la liste.||Élément n°{numero} : ||texte"
			txt = txt.split("||")
			nb = saisir("{}\nNombre d'éléments de la liste : ".format(txt[0]), "entier")
			for i in range(nb):
				var.append(saisir(txt[1].format(numero=i+1), txt[2]))
		elif type_var == "tuple":
			var = []
			if txt == ">>> ":
				txt = "Aucune information sur le tuple.||Élément n°{numero} : ||texte"
			txt = txt.split("||")
			nb = saisir("{}\nNombre d'éléments du tuple : ".format(txt[0]), "entier")
			for i in range(nb):
				var.append(saisir(txt[1].format(numero=i+1), txt[2]))
			var = tuple(var)
		elif type_var == "dictionnaire":
			if txt == ">>> ":
				txt = "Aucune information sur le dictionnaire.||Clé n°{numero} : ||Valeur n°{numero} (correspondant à {cle}) : ||texte"
			txt = txt.split("||")
			var = {}
			nb = saisir("{}\nNombre d'éléments du dictionnaire : ".format(txt[0]), "entier")
			for i in range(nb):
				Cle = saisir(txt[1].format(numero=i+1), txt[3])
				var[Cle] = saisir(txt[2].format(numero=i+1, cle=Cle), txt[3])
	except ValueError:
		print("Erreur : Veuillez saisir une variable de type \"{}\".".format(type_var))
		return saisir(txt, type_var)

	return var

def dessiner(axiome="F+F--F+F", longueur=10, vitesse=0, couleur="blue", position=[(0, 0), 0], angle=60, unique=True, lettres=["F"]):
	"""
	Fonction de dessin (via le module "Turtle") de l'axiome itéré.
	Les paramètres par défaut dessinent le Flocon de Koch.

	axiome : Axiome itéré
	longueur : Taille d'un segment | Défaut = 10
	vitesse : Vitesse de déplacement de la tortue | "fastest" = 0, "fast" = 10, "normal" = 6, "slow" = 3, "slowest" = 1 | Défaut = 0
	couleur : Couleur du trait | Défaut = "blue"
	position : Position de départ de la tortue | Doit être une liste dont le premier élément est un tuple contenant les coordonnés (x, y) et le second la direction | Défaut = [(0, 0), 0]
	angle : Mesure d'un angle en degrés
	unique : Si activé, s'arrête après avoir dessiné la figure | Défaut = True
	lettres : Caractère(s) signifiant "avancer" | Doit être une liste
	"""

	i = 0
	balise = []
	fenetre = turtle.Screen()
	crayon = turtle.Turtle()
	crayon.hideturtle()
	crayon.speed(0)
	if couleur != "multicolor" and couleur != "mc":
		crayon.pencolor(couleur)
	if position[0] != (0, 0):
		crayon.up()
		crayon.goto(position[0])
		crayon.down()
	if position[1] != 0:
		crayon.seth(position[1])

	for c in axiome:
		if couleur == "multicolor" or couleur == "mc":
			crayon.pencolor(colorsys.hls_to_rgb(i/len(axiome), 0.5, 1.0))
			i += 1
		if c == "+":
			crayon.left(angle)

		if c == "-":
			crayon.right(angle)

		if c == "[":
			balise.append((crayon.pos(), crayon.heading()))

		if c == "]":
			loc, facing = balise.pop()
			crayon.up()
			crayon.goto(loc)
			crayon.seth(facing)
			crayon.down()

		if c in lettres:
			crayon.forward(longueur)

	if unique == True:
		turtle.mainloop()

def iterer(axiome="F", quantite=3, signes=["+", "-"], lettres={"F":"F+F--F+F"}):
	"""
	Fonction d'intération de l'axiome.
	Les paramètres par défaut itèrent 3 fois le Flocon de Koch.

	axiome : Axiome de départ
	quantite : Nombre d'intération souhaité | Défaut = 3
	signes : Caractère(s) qui ne doit (doivent) pas être transformé(s) | Doit être une liste | Défaut = ["+", "-"]
	lettres : Caractère(s) qui doit (doivent) être transformé(s) et caractère(s) de remplacement | Doit être un dictionnaire où les clés correspondent aux caractères remplacés et les valeurs aux caractères de remplacement
	"""

	if quantite <= 0:
		return axiome

	for i in range(quantite):
		axiome_itere = ""
		for c in axiome:
			if c in signes:
				axiome_itere += c

			if c in lettres.keys():
				axiome_itere += lettres[c]

		axiome = axiome_itere

	return axiome_itere

def iterer_figure(axiome="A+A+A+A", figures=[1, 7], quantite=3, signes=["+", "-"], lettres={"A+A+A+A":"B+B+B+B+BA+A+A+A++B-B++A+A+A+A+BA+A+A+A", "B":"BB"}):
	"""
	Fonction d'intération de l'axiome.
	Les paramètres par défaut itèrent 3 fois le carré.

	axiome : Axiome de départ
	figures : Nombre de caractère(s) de la (des) figure(s) qui se fait (fond) remplacée(s) | Doit être une liste
	quantite : Nombre d'intération souhaité | Défaut = 3
	signes : Caractère(s) qui ne doit (doivent) pas être transformé(s) | Doit être une liste | Défaut = ["+", "-"]
	lettres : Caractère(s) qui doit (doivent) être transformé(s) et caractère(s) de remplacement | Doit être un dictionnaire où les clés correspondent aux caractères remplacés et les valeurs aux caractères de remplacement
	"""

	if quantite <= 0:
		return axiome

	for i in range(quantite):
		axiome_itere = ""
		axiome_semi_itere = ""
		for j in figures:
			for k in range(len(axiome)-j):
				c = axiome[k:k+j]
				if c in lettres.keys():
					axiome_itere += lettres[c]
				else:
					axiome_itere += c

			axiome_semi_itere += axiome_itere
		axiome = axiome_semi_itere

	return axiome_itere