##Herencia
"""
Poder reutilizar codigo y ahorrar lineas

class Perro(clase de donde hereda):

La clase desde donde herada puede se llama (superClase, clasePrincipal, etc)
La clase que hereda se llama (subClase, claseHija, etc)

En python puede haber herencia multiple, para definirlo solo es necesario
mandar las clases de las que hereda como argumento

	class Perro(clase1, clase2):

En los metodos comunes la lectura de los metodos es de arriba a abajo
y cuando se hereda es de izq a derch, la primera clase que lea será la clase que utilizara su metodo comun
"""


#Clase padre
class Animal:
	def comer(self):
		print("Comiendo")
	def dormir(self):
		print("Durmiendo")
	def comun(self):
		print("Metodo comun de Animal")

class Mascota:
	#Se crea un metodo para poder definir los nuevos atributos
	def fecha_adopcion(self, fecha_adopcion):
		self.fecha_adopcion = fecha_adopcion

	def comun(self):
		print("Metodo comun de Mascota")


#Clase hija
class Perro(Animal, Mascota):

	def __init__(self, nombre):
		self.nombre = nombre

	def ladrar(self):
		print("Ladrando")

	def comun(self):
		print("Metodo comun de perro")


class Gato(Animal):

	def __init__(self, nombre):
		self.nombre = nombre

	def ronronear(self):
		print("grrrrrrrrr! UwU")




anuk = Perro("Anuk")
anuk.comun()


"""
anuk = Perro("Anuk")
anuk.fecha_adopcion("Hoy")
print(anuk.fecha_adopcion)
"""
#anuk.comer()
#anuk.dormir()
#anuk.ladrar()

"""
gardfield = Gato("Gardfield")
gardfield.dormir()
gardfield.ronronear()
gardfield.comer()
"""
