##Riman

#Declaramos nuestras listas y variables necesarias
lista = []
numVoca = 0

def get_datos():

	for i in range(2):

		#El string que se ingresa lo casteamos a lista y separamos cada caracter
		print("Ingresa tu ", i+1, "° palabra")
		string = input()
		newstring = "".join(string)
		#print(newstring)
		newstring = newstring.lower()
		newstring = list(newstring)

		#print(newstring)

		lista.append(newstring)

#	print(lista)
	return lista


def get_caract(list, num):

	ultimas = []

	for i in range (2):
#		print("Desde -> ", len(list[i]), "Hasta ->", len(list[i])-num)
		for j in range (len(list[i]), len(list[i]) - num, -1):

#			print((list[i])[j-1])
			ultimas.append((list[i])[j-1])


#	print(ultimas)

	return ultimas


def comparar(ulti):

	cont0 = 0
	cont1 = 0

	for i in range(3):

#		print("3)comparamos ", ulti[i] , " y ", ulti[i+3])
		if(ulti[i] == ulti[i+3]):
			cont1 = cont1 + 1


#	print("Valores 3 ->", cont1)
	if(cont1 == 0):

		print("No rima")

	elif(cont1 > 2):

		print("Riman")

	else:

		print("Riman un poco")


listaTest = get_datos()
comparar(get_caract(listaTest, 3))
