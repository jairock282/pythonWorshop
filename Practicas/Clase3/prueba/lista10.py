##Lista de 10

#Creamos nuestra lista
lista = []
num = 0
sumaTotal = 0
promedio = 0
numMayor = 0
numMenor = 0

#Recorremos nuestro ciclo
for i in range(10):

	print("Ingresa tu ", i, "° numero> ")
	num = input()
	lista.append(num)

	sumaTotal += int(num)



print("La suma de todos los numeros es: ", sumaTotal)
print("El promedio es: ", (sumaTotal / len(lista)))

##Ordenamos la lista
lista.sort()
print(lista)
print("El numero mayor es: ", max(lista))
print("El numero menor es: ", min(lista))
