##Cuenta

class Cuenta:


	##Atributos
	def __init__(self, cuenta = 0):

		self.cuenta = cuenta


	def retirar(self, num):

		if((self.cuenta - num) < 0):

			print("Se realizo el retiro")
			self.cuenta = 0

		else:
			print("Se realizo el retiro")
			self.cuenta = self.cuenta - num


	def ingresar(self, num):

		if(num > 0):

			self.cuenta = self.cuenta + num

			print("Se ingreso la cantidad")


cuenta1 = Cuenta()
cuenta1.ingresar(-5)
print("Saldo actual ->", cuenta1.cuenta)
cuenta1.retirar(500)
print("Saldo actual ->", cuenta1.cuenta)
