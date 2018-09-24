##Funciones anidadas

def comenzar_play_list(lista):

	def reproducir():

	#Definimos que la variable lista no es solamente local
	#por lo que podra sufrir cambios

		nonlocal lista
		lista = ['track4', 'track5', 'track3']

		for val in lista:

			print(val)
	reproducir()


lista = ['track1', 'track2', 'track3']

comenzar_play_list(lista)

print(lista)

