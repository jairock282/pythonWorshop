def frecuencia(secuencia):

	##Creamos un diccionario
	frec = dict()

	##Verificamos la existencia de los elementos en el diccionario
	for elementos in secuencia:
		frec[elementos] = frec.get(elementos, 0) + 1

	print(frec)

frecuencia(["peras", "manzanas", "peras"])
frecuencia((1,3,4,3,2,1))
