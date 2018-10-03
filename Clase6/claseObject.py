##Herencia
"""
En python todas las clases heredan por default de la clase Object, la cual,
cuenta con un alista de atributos y metodos para poder utilizar

__init__ no es un constructor, solo es un metodo que permite definir 
los atributos



"""

class Gato:

	def __init__(self, nombre):
		self.nombre = nombre

	#Metodo que nos permitira regresar el atributo que hace referencia
	#al objeto, es similar a los getters y setters en java
	def __str__(self):
		return self.nombre

class Pato(object):
	def __init__(self, nombre):
		self.nombre = nombre
	def __str__(self):
		return self.nombre


gato = Gato("Gardfield")
gato.edad = 6
pato = Pato("Lucas")

"""
print(gato)
print(pato)
"""

##Con el metodo __dict__ nos regresara un diccionario con los valores
#correspondientes
print(gato.__dict__)
print(pato.__dict__)
