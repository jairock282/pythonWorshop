##Password
class Password:

	listMayus = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','X','Z']
	listMinus = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','x','z']
	listNum = ['0','1','2','3','4','5','6','7','8','9']


	def __int__(self, longitud = 8, contraseña = ''):

		self.longitud = longitud
		self.contraseña = contraseña

	def generar_Password(self, pas):

		lon = len(pas)
		self.contraseña = pas
		self.longitud = lon

		print("Se ha asignado la contraseña y la longitud")

	@classmethod
	def es_fuerte(cls, pas, lon):

		es = False
		contMayus = 0
		contMinus = 0
		conNum = 0
		i = 0
		pas = list(pas)

#		print("Largo -> ", len(pas))
		for i in range(0,len(pas),1):

			#print("i ->", i)

			if(pas[i] in cls.listMayus):

				contMayus = contMayus + 1

			if(pas[i] in cls.listMinus):

				contMinus = contMinus + 1

			if(pas[i] in cls.listNum):

				conNum = conNum + 1

#		print("CantMayus -> ", contMayus)
#		print("CantMinus -> ", contMinus)
#		print("CantNum -> ", conNum)



		if(contMayus == 2) and (contMinus == 1) and (conNum == 5):

			es = True

		#print("EsFuerte ->", es)
		return es

contra = Password()
contra.generar_Password("QuO23456")

print("------------------------------------")
print("Contra -> " + contra.contraseña)
print("Long -> " + str(contra.longitud))

es = contra.es_fuerte(contra.contraseña, contra.longitud)
print("Es Fuerte -> ", es)
