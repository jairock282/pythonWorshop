##Creamos una lista con nombre
nomList = []
genList = []


print("Cuantos nombres desea ingresar? ")
num = int(input())

for i in range(num):
	#Ingresamos los valores
	print("Ingrese el ", i+1,"° nombre")
	nom = input()
	nomList.append(nom)

#Transformamos la lista en tupla
nombre = tuple(nomList)
for i in range(len(nombre)):

	print("Estimado, ", nombre[i], " vote por mi")

#Preguntamos por el genero
for i in range(len(nombre)):

	print("Genero de", nombre[i],":")
	genList.append(input())

genero = tuple(genList)

nomGen = zip(nombre, genero)
nomGen = tuple(nomGen)

print(nomGen)
