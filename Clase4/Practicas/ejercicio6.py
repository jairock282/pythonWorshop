##Tupla de edades
listEdad = []

def get_edad():

	for i in range(10):
		print("Ingresa tu ", i+1, "° edad")
		listEdad.append(int(input()))

#edades = (1,20,30,40,50,60,7,8,9,10)


def mayor_20():

	get_edad()
	cant = 0
	tuplaEdad = tuple(listEdad)

	for i in range(10):

		#print(tuplaEdad[i])
		if(tuplaEdad[i] > 20):
			#print("Entro")
			cant = cant + 1
			#print("Cant -> ", cant)

	print("Personas con edad superior a 20 -> ", cant)



mayor_20()
