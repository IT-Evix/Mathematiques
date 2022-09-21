import math

def SommeSuiteGeometrique():
	u0=input("Est-ce que vous cherchez la somme des n+1 premiers termes (U0) ? Répondre par oui ou par non ")
	u1=input("Est-ce que vous cherchez la somme des n premiers termes (U1)? Répondre par oui ou par non ")

	if u0==("oui") :
		u=float(input("U0 = ? "))
		n=int(input("nombre de termes n ? "))
		q=float(input("raison q ? "))
		s=u*((1-q**(n+1))/(1-q))
		print("S= ",s)
	elif u0==("non"):
		print("")
	else:
                print("Erreur chercher U0 ou U1 avant de lancer le programme")

	if u1==("oui") :
		u=float(input("U1 = ? "))
		n=int(input("nombre de termes n ? "))
		q=float(input("raison q ? "))
		s=u*((1-q**n)/(1-q))
		print("S= ",s)
	elif u1==("non"):
		print("")
	else:
		print("Erreur chercher U0 ou U1 avant de lancer le programme")

SommeSuiteGeometrique()
