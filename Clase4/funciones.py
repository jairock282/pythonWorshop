"""

definir funciones -> las creamos

invocar funciones -> llamarlas

"""

"""
#Crear funciones def nomFuncion
def saludar():

	print("Hola mundo")


#Llamar la funcion
saludar()


def crear_mensaje(nombre):
			#{} recibe argumento
	mensaje = "Hola {}, bienvenido a las funciones".format(nombre)

	return mensaje


nuevo_mensaje = crear_mensaje("Pedrito Sola")

print(nuevo_mensaje)


def suma(val1, val2, val3):

	return (val1 + val2 + val3)


resultado = suma(10,20,30)
print(resultado)



#Regresar varios valores para almacenarlas en varias variables
def obtener_curso():
	return "Curso de Python", "Básico", "3.6"


#Definimos variables que almacenaran los valores que regrese la funcion
nombre, nivel, version = obtener_curso()

print(nombre)
print(nivel)
print(version)


#Esta funcion regresara un diccionario
#por ese motivo lo que se regresa se encuentra entre llaves ya que asi definimos un diccionario

#Los parametros pueden definirse con valores iniciales desde el principio
#Por convencion si se le define un valor inicial se pone sin espacios
def crear_usuario(nombre, apellido, edad=10):

	return {

	'nombre':nombre,
	'apellido':apellido,
	'edad':edad,
	'nombreCompleto': "{} {}".format(nombre, apellido)

	}


#El diccionario que regresamos lo almacenamos en usuario
usuario = crear_usuario("Pedrito", "Sola", 90)

#imprimimos cada valor de cada key
print(usuario["nombre"])
print(usuario["apellido"])
print(usuario["edad"])
print(usuario["nombreCompleto"])


#cuando no tenemos definido el nuemero de argumentos que recibira la funcion
#se utiliza la keyword "*args"
#El * significa que almacenara los valores de argumentos dentro de una tupla

def sumaPro(*args):

	total = 0

	#Vamos iterando las posiciones de la tupla
	for valor in args:
		total = total + valor

	return total


resultado = sumaPro(10, 20, 30, 40, 50)
print(resultado)

#Podemos definir parametros requeridos y ademas utilizar *args
def sumaPro2(parametro_requerido, *args):

	total = 0
	print(parametro_requerido)

	#Vamos iterando las posiciones de la tupla
	for valor in args:
		total = total + valor

	return total


resultado = sumaPro2("Argunmento requerido", 10, 20, 30, 40, 50)
print(resultado)

#Podemos usar multiples argumentos con otra forma

def usuarios_autenticados(**kwargs):

	print(kwargs)

##Como no definimos la cantidad de argumentos podemos colocar los que 
#se necesiten y seran almacenados en un diccionario
usuarios_autenticados(nombre="Raquel", años=24)


##Cuando se usa un * -> se almacena en una tupla
##Cuando se usa ** -> se almacena en un diccionario


def combinacion(requerido, *args, **kwargs):

	print(requerido)
	print(args)
	print(kwargs)

# 10 y 20 estaran dentro de la tupla y los que tienen una key y value se almacenaran en el diccionario
 combinacion("Argumento Requerido", 10, 20, v=True, f=False)

#return a medio camino
def mi_funcion():

	print("mensaje1")
	#Si colocamos un return lo que hara la funcion es deternerse en ese
	#punto y regresar lo que haya hasta el momento
	return

	print("mensaje2")

mi_funcion()

##Funciones con Variables

#Variable global
animal = "Leon"

def mostrar_animal():
#Podemos realizar un cambio directo a la variable global con la palabra global
	global animal
	#Variable local
	animal = "Perro"
	print(animal)

mostrar_animal()
print(animal)

"""
#Funciones lambda -> asiganar una funcion a una variable
#Permiten expresarse en una sola linea de codigo 

#Forma 1
def centigrados_far(grados):
	return (grados * 1.8) + 32

funcion_variable = centigrados_far
resultado = funcion_variable(32)
print(resultado)

#Forma 2
#cuando utilizo una funcion lambda no se necesita realizar un return
#Se pueden determinar los parametros que necesitamos y se delimita con los :
mi_funcion = lambda grados=0: grados * 1.8 + 32
resultado = mi_funcion(32)
print(resultado)

