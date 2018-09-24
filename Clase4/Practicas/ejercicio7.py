##Cantidad de vocales

#Declaramos nuestras listas y variables necesarias
lista = []
numVocaA = 0
numVocaE = 0
numVocaI = 0
numVocaO = 0
numVocaU = 0

#El string que se ingresa lo casteamos a lista y separamos cada caracter
print("Ingresa tu frase")
string = input()
string = string.split()
#print(string)
newstring = "".join(string)
#print(newstring)
newstring = newstring.lower()
newstring = list(newstring)

#print(lista)

largoString = len(newstring)

for i in range(largoString):

	if (newstring[i] == 'a'):

		numVocaA = numVocaA + 1

	elif (newstring[i] == 'e'):

		numVocaE = numVocaE + 1

	elif (newstring[i] == 'i'):

		numVocaI = numVocaI + 1

	elif(newstring[i] == 'o'):

		numVocaO = numVocaO + 1

	elif(newstring[i] == 'u'):

		numVocaU = numVocaU + 1



print("Cantidad de vocales")
print("A -> ", numVocaA)
print("E -> ", numVocaE)
print("I -> ", numVocaI)
print("O -> ", numVocaO)
print("U -> ", numVocaU)


