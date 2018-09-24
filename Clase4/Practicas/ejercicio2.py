#Palabras mas larga

def mas_larga(*args):

	wordList = list(args)
	numPalabras = len(wordList)

	numCaracteresMax = 0
	posMasLarga = 0

	#Realizamos un ciclo para recorrer la lista de palabras
	for i in range(0, numPalabras, 1):

		#En cada posicion de la lista, guardaremos una lista de caracteres 
		#Para poder contar cada uno de los elementos
		wordList[i] = list(wordList[i])

		#Comparamos y vamos almacenando la palabra con mas caracteres
		if (len(wordList[i]) >= numCaracteresMax):

			#Almacenamos la posicion de la palabra
			posMasLarga = i
			#Asignamos la nueva cantidad mas grande
			numCaracteresMax = len(wordList[i])

	#Volvemos a hacer string la lista de caracteres que definimos como mas grande
	palabra = " ".join(wordList[posMasLarga])

	#Devolvemos el string
	print("La palabra mas larga es: ", palabra)


mas_larga("Queondaquepexxddxx", "on", "que", "pex", "wuw", "u")
