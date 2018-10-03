##Gestion de empleados
class EmpleadoComercial:

	sumaPlus = 300

	def __init__(self, nombre='', edad='', salario=''):

		self.nombre = nombre
		self.edad =  edad
		self.salario = salario

	@classmethod
	def plus(cls, edad, salario):

		seHace = False

		if (edad > 30):

#			print("Es mas que un treinton")

			if (salario > 200):

#				print("Su salario es mas que 200")
				seHace = True
				mas = cls.sumaPlus
				salario = salario + mas

		return seHace
#		print("El salario para este comerciante con su plus es ->", salario)

class EmpleadoRepartidor:

	sumaPlus = 300

	def __init__(self, nombre='', edad='', salario='', zona=''):

		self.nombre = nombre
		self.edad =  edad
		self.salario = salario
		self.zona = zona

	@classmethod
	def plus(cls, edad, zona, salario):

		seHace = False

		if (edad < 25):

			if (zona == 3):

				seHace = True
				mas = cls.sumaPlus
				salario = salario + mas

		return seHace
#		print("El salario para este repartidor con su plus es ->", salario)


comerciante = EmpleadoComercial("Jaime", 50, 220)
repartidor = EmpleadoRepartidor("Juan", 20, 220, 2)


print("Se hace plus a comerciante -> ", comerciante.plus(comerciante.edad, comerciante.salario))
print("Se hace plus a repartidor -> ", repartidor.plus(repartidor.edad, repartidor.zona, repartidor.salario))
