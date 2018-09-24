#Cuantos años

nomPersonas = []
naciPersonas = []


def datos():

	for i in range(3):

		print("Ingresa el nombre de la ", (i+1),"° persona")
		nombre=input()
		nomPersonas.append(nombre)

		print("Ingresa el año de nacimiento")
		naci=int(input())
		naciPersonas.append(naci)

def get_edad(nombre, naci, agnoCur):

	newEdad = agnoCur - naci

	print(nombre, "cumplira ", newEdad, "este año") 



def calc_edad():

	agno = 0
	print("Ingresa el año en curso")
	agno = int(input())
	datos()

	for i in range(3):

		get_edad(nomPersonas[i], naciPersonas[i], agno)



calc_edad()
