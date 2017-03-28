print ("--intervalo de los cuadrados de n números mayores a 100--")
inicio=input("ingrese el inicio del intervalo")
final=input("ingrese el final del intervalo")

def cuadrados():
	suma =0.0
	final2=int(final)
	inicial2=int(inicio)
	lista=[]
	for i in range(inicial2,final2+1):
		num=i**2
		if num > 100:
			lista.append(num)
		else:
			print ("el numero", i, "a la potencia 2 no es mayor a 100", num)
			print ("numeros a la potencia 2 mayores a 100: ", lista)

cuadrados()			

    
    
