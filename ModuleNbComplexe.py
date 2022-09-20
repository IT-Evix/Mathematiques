import math

Re=float(input("Entrer la partie reelle de z: "))
Img=float(input("Entrer la partie imaginaire de z sans i avec son signe (+ ou -): "))

print("z = ",Re,"+(",Img,")i ")

def calculModule(Re,Img):
	module=math.sqrt(Re*Re+Img*Img)
	print("z a pour module :", module)
	return 0
calculModule(Re,Img)
