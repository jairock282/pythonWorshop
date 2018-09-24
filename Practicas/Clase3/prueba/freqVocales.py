##Cantidad de vocales

#Declaramos nuestras listas y variables necesarias
lista = []
numA = 0
numE = 0
numI = 0
numO = 0
numU = 0

A = False
E = False
I = False
O = False
U = False

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

	#print(i)

	if newstring[i] == 'a':

		numA = numA + 1

		A = True

	elif newstring[i] == 'e':

		numE = numE + 1

		E = True


	elif newstring[i] == 'i':

		numI = numI + 1

		I = True


	elif newstring[i] == 'o':

		numO = numO + 1

		O = True


	elif newstring[i] == 'u':

		numU = numU + 1

		U = True



print("Frecuencia de las Vocales")

if A == True:
	print("A -> ", numA)
if E == True:
	print("E -> ", numE)
if I == True:
	print("I -> ", numI)
if O == True:
	print("O -> ", numO)
if U == True:
	print("U -> ", numU)
