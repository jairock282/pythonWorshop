"""
Practica 8
Papel, boligrafo, marcador

*Escribir una clase Papel que contenga un texto, un metodo escribir, que reciba una cadena para agregar al texto, y el metodo __str__ que imprima el contenido
del texto.

*Escribir una clase boligrafo que contenga una cantidad de tinta, y un metodo escribir, que reciba un texto y un papel sobre el cual escribir. 
Cada letra escrite debe reducir la cantidad de tinta contenida. Cuando la tinta se acabe, debe lanzar una excepción.

*Escribir la clase marcador que herede de boligrafo, y agregue el método recargar, que reciba la cantidad de tinta a aagregar
"""

class Papel:

	##Inicializamos los atributos del objeto
	def __init__(self):
		self.texto = None

	def escribir(self, text):
		self.texto = text

	##Regresamos el objeto como un string
	def __str__(self):
		return self.texto


class Boligrafo:

	def __init__(self):
		self.ink = 100
		self.gasto = 0

	def __str__(self):
		return 'Cantidad de tinta ' + str(self.ink) + '%'

	def escribir(self, obj, text):
		caracteres = text.split(" ")
		newCa = "".join(caracteres)
		numCa = len(list(newCa))
		#print(newCa)
		self.gasto = numCa
		print("Escribiste -> " + text)

	def restaTinta(self):

		cantLetras = self.gasto
		##Cantidad de tinta a perder por letra 5%
		inkLess = cantLetras * 5

		if( self.ink - inkLess > 0):
			print("Perdera " + str(inkLess) + "% de tinta")
			self.ink = self.ink - inkLess
			print("Actualizacion cantidad tinta -> " + str(self.ink) + '%')
		elif(self.ink - inkLess == 0):
			print("Perdera " + str(inkLess) + "% de tinta")
			self.ink = self.ink - inkLess
			print("Se ha agotado la tinta")
		else:
			print("No cuenta con suficiente tinta")

class Marcador(Boligrafo):

	def llenarTinta(self, cantidad):

		if(self.ink + cantidad >= 100):
			self.ink = 100
			print("Se ha rellenado completamente la tinta")
		elif(self.ink + cantidad < 100):
			self.ink = self.ink + cantidad
			print("Nivel actual de tinta -> " + str(self.ink) + "%")
		else:
			print("Cantidad no valida")

##Papel
p = Papel()
p.escribir("papelito")
print(p)

#Boligrafo
b = Boligrafo()
b.escribir(p, "Que onda que pex")
b.restaTinta()

#Marcador
m = Marcador()
m.escribir(p, "Hola soy el marcador")
m.restaTinta()
m.llenarTinta(20)






