print ("--intervalo de n numeros entre 20 y 60--")
print (" ")

def inter():
	num=int(input("ingrese la cantidad de numeros a usar en el intervalo"))
	lista=[]
	for i in range(20,(20+num)+1):
		lista.append(i)
		print (lista)
inter()