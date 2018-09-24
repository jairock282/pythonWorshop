##Clases
"""
Clase 5:

	Objeto → cualquier objeto
		contiene: metodos y atributos

	Clase → molde de donde derivan los objetos

	En python todo es un objeto

"""


#Crear una clase
"""
#Para las clases se utiliza camelCase
class Usuario:
	#Creamos metodo
	#Por convencion al parametro del metodo se le llama self
	def saludar(self, nombre):
		print("Tons khe ", nombre ,"?")

#Creando un objeto de la clase
jose = Usuario()
pepe = Usuario()


#Para saber de que clase es, que tipo de objeto es, etc se utiliza type()
print(type(jose))
print(type(pepe))


jose.saludar("Jose Perez")
pepe.saludar("Jose Sanchez")
"""

###############################################################################################

"""
##Se puede tener atributos dentro y fuera de la clase
class Usuario:
	#Creamos metodo
	#Por convencion al parametro del metodo se le llama self para poder hacer referencia al objeto
	def saludar(self, nombre):
		print("Tons khe ", nombre ,"?")


	def crear_nombre(self, nombre):
		self.nombre = nombre

	def mostrar_nombre(self):
		print(self.nombre)

jose = Usuario()
##Definiendo atributo fuera de la clase
#jose.username = "Jose Perez"
#jose.correo = "jose@gmail.com"

pepe = Usuario()
##Definiendo atributo fuera de la clase
#pepe.username = "Pepe Sanchez"
#pepe.correo = "elPepe@gmail.com"


jose.crear_nombre("Jose Sanchez")
pepe.crear_nombre("El pepe")

jose.mostrar_nombre()
"""


###############################################################################
#Inicializar atributos dentro de la clase
"""
class Usuario:

	#Poder inicializar los atributos
	def __init__(self, username='', correo='', nombre=''):

		self.username = username
		self.correo = correo
		self.nombre = nombre

	#Creamos metodo
	#Por convencion al parametro del metodo se le llama self para poder hacer referencia al objeto
	def saludar(self):

		#Podemos obtener el nombre ya que es un atributo definido en init
		return "Tons khe "+ self.nombre +"?"


jose = Usuario("JS", "Jose@gmail.com", "Jose Sanchez")
pepe = Usuario()


resultado = jose.saludar()
print(resultado)
"""

################################################################
##Creando atributos de instancia
#Atributos de instancia -> atributos que le pertenecen a la instancia, cada uno de ellos son independietes a cada instancia(objeto)
#Variables de clase -> le pertenecen a la clase y al mismo tiempo pueden ser usadas por las distintas instancias
"""
class Circulo:

	pi = 3.14159265 #variable de clase

	def __init__(self, radio):
		self.radio = radio #Variable de tipo instancia


circulo_a = Circulo(10)
circulo_b = Circulo(20)

print(circulo_a.radio)
print(circulo_b.radio)

print(circulo_a.pi)
print(circulo_b.pi)

##Podemos acceder a una variable de clase sin necesidad de realizar una instancia
print(Circulo.pi)
"""

########################################################################
##Metodos estaticos y de clase

#Metodos estaticos -> se pueden utilizar sin necesidad de realizar una instancia
#Dentro de un metodo estatico se pueden utilizar variables de clase


##Metodo estatico
"""
class Triangulo:

	#Variable de clase
	numero = 2

	##Definimos un metodo esttico
	@staticmethod
	##Como no necesita una instancia(no hay atributos) no se coloca self y se pone directamente los parametros
	def area(base, altura):

		return( (base * altura) / Triangulo.numero)


resultado = Triangulo.area(10, 20)
print(resultado)
"""

##Metodo de clase
#Se utilizara cuando se necesiten variables de clase

class Circulo:

	pi = 3.14159265 #variable de clase

	#Definir que es un metodo de clase
	@classmethod
		#Se define cls para hacer referencia al metodo dentro de la clase
	def area(cls, radio):
		return cls.pi * radio**2


resultado = Circulo.area(5)
print(resultado)
