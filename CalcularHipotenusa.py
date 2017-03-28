import math
print ("--calcular la hipotenusa de un triángulo rectángulo--")
print (" ")
catA = float(input("igrese el valor del cateto A"))
catB = float(input("ingrese el valor del catebo B"))
def hipo (A,B):
	hipotenusa=(A**2)+(B**2)
	hipotenusa=math.sqrt(hipotenusa)
	hipotenusa=float(hipotenusa)
	print ("la hipotenusa es: " , hipotenusa)

hipo(catA,catB)
