##IMPLEMENTACION SINGLETON

#En python no se puede hacer constructores privados
class soyUnico(object):

	#Para determinar que es privada la clase se usa doble guion bajo
	class __soyUnico:

		def __init__(self):
			self.nombre = None

		##Cambiar a string el objeto
		def __str__(self):
			return 'self' + ' ' + self.nombre

	##Creamos una instancia dentro de la misma clase
	instance = None

	def __new__(cls):
		##Controlamos la existencia de las instancias

		if not soyUnico.instance:
			soyUnico.instance = soyUnico.__soyUnico()
		return soyUnico.instance

	##Creamos getters y setters

	def __getattr__(self, nombre):
		return getattr(self.instance, nombre)

	def __setattr__(self, nombre, valor):
		return setattr(self.instance, nombre, valor)




############### CREAMOS INSTANCIAS


personaUnica = soyUnico()
personaUnica.nombre = "Soy unica y detergente"
print(personaUnica)
##Obtener direccion de memoria -> funcion id
print(id(personaUnica))

otraPersona = soyUnico()
otraPersona.nombre = "Soy otra persona"
print(otraPersona)
##Obtener direccion de memoria -> funcion id
print(id(otraPersona))

