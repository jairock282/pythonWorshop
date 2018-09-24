#Filtrar palabras

def print_palabras(list, numPalabras):

	for i in range(0, numPalabras, 1):

		print(list[i])



def mas_larga(num, *args):

#	print("Numero ingresado -> ", num)

	wordList = []

	#Tomamos los valores de args
	for palabra in args:

		wordList.append(palabra)


#	print(wordList)

        #wordList = list(args)
	numPalabras = len(wordList)
	numCaracteres = num

	cantFiltradas = 0
	filtradas = []
        #Realizamos un ciclo para recorrer la lista de palabras
	for i in range(0, numPalabras, 1):

                #En cada posicion de la lista, guardaremos una lista de caracteres
                #Para poder contar cada uno de los elementos
		wordList[i] = list(wordList[i])

                #Comparamos y vamos almacenando la palabra con mas caracteres
		if (len(wordList[i]) > numCaracteres):

			#print("PalabraFiltrada ->", wordList[i])
			filtradas.append("".join(wordList[i]))
			cantFiltradas = cantFiltradas + 1


	print_palabras(filtradas, cantFiltradas)


mas_larga(2, "Queondaquepexxddxx", "on", "que", "pex", "wuw", "u")

