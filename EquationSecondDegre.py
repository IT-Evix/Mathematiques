import math

try:
	a = float (input("Quelle est la valeur de a ?"))
except ValueError:
        print("Erreur il faut entrer un nombre à virgule.")
try:
	b = float (input("Quelle est la valeur de b ?"))
except ValueError:
        print("Erreur il faut entrer un nombre à virgule.")
try:
	c=float (input("Quelle est la valeur de c ?"))
except ValueError:
        print("Erreur il faut entrer un nombre à virgule.")

def calculeDelta (a,b,c):
	return b*b-4*a*c

def resoudreEquation(a,b,c):
	delta = calculeDelta(a,b,c)
	print("delta = ", delta)
	if delta>0:
		racineDelta=math.sqrt(delta)
		print("Donc x1= ",(-b-racineDelta)/(2*a))
		print("et x2= ",(-b+racineDelta)/(2*a))
	elif delta==0:
		print("x0= ",(-b)/(2*a))
	else:
		print("pas de solutions dans R")
	return  0
resoudreEquation(a,b,c)
