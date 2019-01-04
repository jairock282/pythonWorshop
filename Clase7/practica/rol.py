class Personaje:

	def __init__(self, nombre):
		self.nombre = nombre
		self.vida = 100
		self.posicion = ''
		self.velocidad = 20

	def recibir_ataque(self, daño):
		print("Ouch!, has recibido un ataque con " + str(daño) + "% de daño")
		reducir = self.vida - daño

		if(reducir < 100 and reducir > 0):
			print("Vida actual -> " + str(reducir))
			self.vida = reducir
		else:
			print("Tu personaje ha muerto :c")
			self.vida = 0

	def mover(self, direccion, cantidad):

		distancia = self.velocidad * cantidad

		print("Tu personaje se movera hacia " + str(direccion) + " una distancia de "+ str(distancia))

		pos = "".join(str(distancia) + "mts a " + str(direccion))

		print(pos)
		self.posicion = pos


class Soldado(Personaje):

	def atacar(self, obj, daño):
		print("baia baia, has atacado a " + obj.nombre)

		reducir = obj.vida - daño

		if(reducir < 100 and reducir > 0):
			print("Vida actual -> " + str(reducir))
			obj.vida = reducir
		else:
			print("Tu personaje ha muerto :c")
			obj.vida = 0


class Campesino(Personaje):

	def __init__(self, nombre):
		self.nombre = nombre
		self.cosecha = 0

	def cosechar(self, cant):

		print(self.nombre + " has cosechado " + str(cant) + "kilos ")
		self.cosecha = self.cosecha + int(cant)
		print("Cosecha actual -> " + str(self.cosecha))

##Personaje
per = Personaje("Pepe")
per.recibir_ataque(30)
per.mover("izq", 10)

##Soldado
sol = Soldado("Rambo")
sol.atacar(per, 20)

##Campesino
cam = Campesino("Juan")
cam.cosechar(30)
