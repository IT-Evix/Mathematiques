import math

def calculModule(Re,Img):
	module=math.sqrt(Re*Re+Img*Img)
	print("z a pour module :", module)
	return module

def calculTetaExpo(Re,Img):
	r=calculModule(Re,Img)
	cosTeta=Re/r
	sinTeta=Img/r
	tanTeta=Img/Re
	print("cos(Teta)= ",cosTeta, "sin(Teta)= ",sinTeta,"tan(Teta)= ",tanTeta)
	arccosTeta=math.acos(cosTeta)
	arcsinTeta=math.asin(sinTeta)
	arctanTeta=math.atan(tanTeta)
	print("Teta(arccos)= ",arccosTeta,"Teta(arcsin)= ",arcsinTeta,"Teta(arctan)= ",arctanTeta)
	print("Forme trigonométrique de z : ",r,"(cos(",arccosTeta,")+ i sin(",arcsinTeta,")")
	print("Forme exponentielle de z : ",r,"e",math.power(

def formeExpo(Module,Teta):
	print(calculModule(Re,Img))

Re=float(input("Entrer la partie reelle de z: "))
Img=float(input("Entrer la partie imaginaire de z sans i avec son signe (+ ou -): "))
print("z = ",Re,"+(",Img,")i ")

