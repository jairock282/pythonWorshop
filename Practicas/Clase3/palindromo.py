##Es palindroma

print("Cuantas frases quieres ingresar: ")
num = int(input())

#Realizamos las rpeticiones necesarias a la cantidad de frases ha ingresar
for i in range(num):

	#Declaramos nuestras listas y variables necesarias
	lista = []
	stringBW  = []
	num = 0
	numPali = 0

	#El string que se ingresa lo casteamos a lista y separamos cada caracter
	print("Ingresa tu ", i+1, "° frase")
	string = input()
	string = string.split()
	newstring = " ".join(string)
	newstring = list(newstring)
	lista.append(newstring)

	largoString = len(newstring)

	print(newstring)

	#Voltemos la lista y la guardamos en una nueva en orden inverso
	for i in range(largoString, 0, -1):

		stringBW.append(newstring[i-1])


	#Comparamos cada caracter
	for i in range(0, largoString, i):

		if newstring[i] == stringBW[i]:

			numPali = numPali + 1


	#Si la cantidad de caracteres iguales corresponde al tamaño de la palabra es palindromo
	if numPali == largoString:

		print("Es palindromo")

	else:

		print("No es palindromo")


