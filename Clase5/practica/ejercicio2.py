##Password

class Password:

	listMayus = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','X','Z']
	listMinus = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','x','z']
	listNum = [0,1,2,3,4,5,6,7,8,9]

	def __int__(self, longitud = 8, contraseña = ''):

		self.longitud = longitud
		self.contraseña = contraseña

	def es_fuerte(self, pas, lon):

		es = False
		contMayus = 0
		contMinus = 0
		conNum = 0

		lon = list(lon)

		for i in range(0,len(lon),i):

			if(lon[i] in listMayus):

				contMayus = contMayus + 1

			if(lon[i] in listMinus):

				contMinus = contMinus + 1

			if(lon[i] in listNum):

				conNum = conNum + 1

		if(contMayus == 2) and (contMinus == 1) and (conNum == 5):

			se = True

		return es


	def generar_Password(self, pas):

		lon = len(pas)
		self.contraseña = pas
		self.longitud = lon

		print("Se ha asignado la contraseña y la longitud")


contra = Password()
contra.generar_Password("Queonda")
print("Contra -> " + contra.contraseña)
print("Long -> " + str(contra.longitud))
