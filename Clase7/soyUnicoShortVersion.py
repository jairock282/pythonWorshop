##IMPLEMENTACION SINGLETON

#En python no se puede hacer constructores privados
class soyUnico(object):

	##Instancia privada inicializado en none
	__instance = None
	##Aributo nombre
	nombre = None

	##Cambiar objeto a string
	sef __str__(self):
		return 'self' + self.nombre

	##Metodo new para crear la instancia  bajo cierta condicion
	def __new__(cls):
		##Si la instancia no exista
		if not soyUnico.__instance is None:
			##Se crea un objeto con este mismo metodo
			soyUnico.__instance = object.__new__(cls)
		return soyUnico.__instance



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

