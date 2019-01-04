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

		print("Información del objeto")

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


disco = Multimedia("Rammstein", "CD", "Rammstein", "1h40min")
##disco.setFormat("CD")

print(disco)

disco.atributos()

print(Multimedia.iguales(disco))
