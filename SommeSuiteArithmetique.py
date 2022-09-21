import math

def SommeArithmetique():
	u0=input("Est-ce que vous cherchez la somme des n+1 premiers termes ? Répondre par oui ou par non ")
	u1=input("Est-ce que vous cherchez la somme des n premiers termes ? Répondre par oui ou par non ")

	if u0==("oui") :
		u=float(input("U0 = ? "))
		n=int(input("nombre de termes n : "))
		un=float(input("Un = ?"))
		s=(n+1)*(u+n)/2
		print("S= ",s)
	elif u0==("non"):
		print("")
	else:
                print("Erreur chercher U0 ou U1 avant de lancer le programme")

	if u1==("oui") :
		u=float(input("U0 = ? "))
		n=int(input("nombre de termes n : "))
		un=float(input("Un = ?"))
		s=n*((u+n)/2)
		print("S= ",s)
	elif u1==("non"):
		print("")
	else:
		print("Erreur chercher U0 ou U1 avant de lancer le programme")



SommeArithmetique()



#Formules
#(n+1)*(u0+un)/2
#n*((u0+un)/2)
