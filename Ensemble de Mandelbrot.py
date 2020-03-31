from cmath import sqrt
from math import ceil
from colorsys import hls_to_rgb
import turtle as tu
from time import time

def Mandelbrot(n = 50, coords = {"x": {"min": -2, "max": 0.9}, "y": {"min": -1.2, "max": 1.2}}, format_time = False):
	"""
	Fonction qui dessine l'ensemble de Mandelbrot avec n**2 points.
	Renvoie un tuple contenant :
	- Le temps d'execution en secondes si format_time == False (défaut) ou sous la forme "heures:minutes:secondes" si format_time == True ;
	- La vitesse moyenne de placement des points (en points par seconde).
	"""
	start = time()
	fenetre = tu.Screen()
	crayon = tu.Turtle()
	crayon.hideturtle()
	crayon.speed(0)
	crayon.up()
	
	pasx = (coords["x"]["max"] - coords["x"]["min"]) / n
	pasy = (coords["y"]["max"] - coords["y"]["min"]) / n
	
	x = coords["x"]["min"]
	while x < coords["x"]["max"]:
		y = coords["y"]["min"]
		while y < coords["y"]["max"]:
			c = x + sqrt(-1) * y
			z = c
			m = 0
			while abs(z) < 2 and m < 30:
				z = z**2 + c
				m += 1
			crayon.goto(ceil(3 * x / pasx), ceil(3 * y / pasy))
			crayon.dot(4, hls_to_rgb(m / 60 + 0.5, 0.5, 1.0))
			y += pasy
		x += pasx
	temps = time() - start
	if format_time:
		temps = ceil(temps)
		sec = temps
		min = 0
		heure = 0
		if temps >= 60:
			sec %= 60
			min = (temps - sec) // 60
		if min >= 60:
			min %= 60
			heure = (temps - min - sec) // 3600
		return "{heure:02}:{min:02}:{sec:02}".format(heure = heure, min = min, sec = sec), n**2 / temps
	else:
		return temps, n**2 / ceil(temps)

perfs = Mandelbrot(n = int(input("n = ")), format_time = True)
print("Temps de réalisation : {temps}.\nSoit en moyenne {pts_par_sec} points par seconde.".format(temps = perfs[0], pts_par_sec = perfs[1]))
tu.mainloop()