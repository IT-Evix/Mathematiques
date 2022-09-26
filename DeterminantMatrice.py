import math

def calculDeterminant():

	m2=input("Souhaitez vous calculer le déterminant d'une matrice 2x2 ? Répondre par oui ou non. ")
	m3=input("Souhaitez vous calculer le déterminant d'une matrice 3x3 ? Répondre par oui ou non. ")


	if (m2=="oui"):
		coef1=float(input("Quel est le nombre de la matrice première ligne, première colonne ? "))
		coef2=float(input("Quel est le nombre de la matrice première ligne, deuxième colonne ? "))
		coef3=float(input("Quel est le nombre de la matrice deuxième ligne, première colonne ? "))
		coef4=float(input("Quel est le nombre de la matrice deuxième ligne, deuxieme colonne ? "))
		print("La matrice est ")
		print("[",coef1," ",coef2,"]")
		print("[",coef3," ",coef4,"]")
		det=coef1*coef4-coef2*coef3
		print("Le déterminant de cette matrice est : ",det)
	else:
		print(" ")

	if (m3=="oui"):
		coef1=float(input("Quel est le nombre de la matrice première ligne, première colonne ? "))
		coef2=float(input("Quel est le nombre de la matrice première ligne, deuxième colonne ? "))
		coef3=float(input("Quel est le nombre de la matrice première ligne, troisième colonne ? "))
		coef4=float(input("Quel est le nombre de la matrice deuxième ligne, première colonne ? "))
		coef5=float(input("Quel est le nombre de la matrice deuxième ligne, deuxieme colonne ? "))
		coef6=float(input("Quel est le nombre de la matrice deuxième ligne, troisième colonne ? "))
		coef7=float(input("Quel est le nombre de la matrice troisième ligne, première colonne ? "))
		coef8=float(input("Quel est le nombre de la matrice troisième ligne, deuxième colonne ? "))
		coef9=float(input("Quel est le nombre de la matrice troisième ligne, troisième colonne ? "))
		det=coef1*(coef5*coef9-coef8*coef6)-coef2*(coef4*coef9-coef7*coef6)+coef3*(coef4*coef8-coef7*coef5)
		print("[",coef1," ",coef2," ",coef3,"]")
		print("[",coef4," ",coef5," ",coef6,"]")
		print("[",coef7," ",coef8," ",coef9,"]")
		print("Le déterminant de cette matrice est : ",det)
	else:
		print(" ")
	return 0

calculDeterminant()
