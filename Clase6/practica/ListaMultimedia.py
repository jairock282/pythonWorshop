class Multimedia:

	formats = ['wav', 'mp3', 'midi', 'avi', 'mov', 'mpg', 'cdAudio', 'dvd']

	def __init__(self, titulo, formato, autor, duracion):

		self.titulo = titulo
		self.formato = formato
		self.autor = autor
		self.duracion = duracion

		self.setFormat(formato)

	##Verificacion y reasignacion del formato
	def setFormat(self, formato):

		if formato in self.formats:
			self.formato = formato
			#print("Entro")
		else:
			print("Formato no valido, vuelva a intentarlo")
			print("Formatos validos = 'wav', 'mp3', 'midi', 'avi', 'mov', 'mpg', 'cdAudio', 'dvd'")
			print("Ingrese el nuevo formato")
			newFormat = input()
			self.setFormat(newFormat)

	##Retornamos los valores de nuestros atributos
	def __str__(self):

		cadena = "\nTitulo: "+self.titulo+" | Autor: "+self.autor+" | Formato: "+self.formato+"| Duracion: "+self.duracion 

		return cadena

	##Devolvemos solo los atributos
	def atributos(self):

		lista = list(self.__dict__)
		print("\nLos atributos de la clase son:")
		print(lista)

	##Verificamos si titulo y autor es el mismo
	@staticmethod
	def iguales(obj):

		es = False

		if obj.titulo == obj.autor:

			es = True

		return es




class ListaMultimedia:

	cont = 0;

	def __init__(self):

		self.arrayMulti = []


	def setMulti(self, obj):

		self.arrayMulti.append(obj)

		self.cont = self.cont + 1

	def lenArray(self):

		tam = str(len(self.arrayMulti))

		print("Cantidad de objetos en la lista: " + tam)

	def giveMeObj(self, pos):

		print("\n\nObjeto de la posicion " + str(pos))
		print(str(self.arrayMulti[pos]))

	def allInfo(self):

		print("\n\nInformacion de los objetos almacenados")
		for i in range(0, self.cont):

			print(self.arrayMulti[i])


disco1 = Multimedia("Rammstein", "wav", "Rammstein", "1h40min")
disco2 = Multimedia("Rammstein", "mp3", "Rammstein", "1h40min")
disco3 = Multimedia("Rammstein", "midi", "Rammstein", "1h40min")

lista = ListaMultimedia()


lista.setMulti(disco1)
lista.setMulti(disco2)
lista.setMulti(disco3)

lista.lenArray()

lista.giveMeObj(2)

lista.allInfo()
