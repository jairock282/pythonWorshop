class Multimedia:

	formats = ['wav', 'mp3', 'midi', 'avi', 'mov', 'mpg', 'cdAudio', 'dvd']

	def __init__(self):

		self.titulo = " "
		self.formato = " "
		self.autor = " "
		self.duracion = " "

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

class Pelicula(Multimedia):

	def __init__(self):

		self.actorPrincipal = " "
		self.actrizPrincipal = " "


	##Asignamos atributos
	def setAtributes(self):

		print("Titulo >")
		titulo = input()
		self.titulo = titulo

		print("Formato >")
		formato = input()
		self.setFormat(formato)

		print("Autor >")
		autor = input()
		self.autor = autor


		print("Duracion >")
		duracion = input()
		self.duracion = duracion


		print("Actor principal >")
		mainActor = input()
		self.actorPrincipal = mainActor

		print("Actriz principal >")
		mainActress = input()
		self.actorPrincipal = mainActress


	##OVERWRITTEN
	##Retornamos los valores de nuestros atributos
	def __str__(self):

		print("Información del objeto")

		cadena = "\nTitulo: "+self.titulo+" | Autor: "+self.autor+" | Formato: "+self.formato+"| Duracion: "+self.duracion+" | Actor Principal: "+self.actorPrincipal+" | Actriz Principal: "+self.actrizPrincipal 

		return cadena



titanic = Pelicula()
titanic.setAtributes()
print(titanic)
