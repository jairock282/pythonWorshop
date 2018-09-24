##for i in range(1, 101, 2):

##	print(i)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
for i in range(len(lista)):

	print("index: ", i, " Valor: ", lista[i])
"""

"""
for indice, valor in enumerate(lista): #Se le puede poner un valor inicial dando un segundo parametro

	print("Indice ", indice, "Valor ", valor)
"""

texto = "Curso de Python Basico"

##Uso del break
"""
for caracter in texto:

	if caracter == "P":
		break

	print(caracter)
"""
##Uso de continue
"""
for caracter in texto:

	if caracter == "P":
		#Cuando se realiza se discrimina la condicion
		#Pero permite que continue el ciclo
		continue

	##Seguira imprimiendo los demas caractares
	print(caracter)
"""

##Acortando filtros

##Modo Largo
"""
calificacion = int(input("Ingrese una calificacion> "))

if calificacion >= 8:

	print("Aprobado")
else:

	print("Reprobado")
"""
##Modo corto
calificacion = int(input("Ingrese una calificacion> "))
resultado =  "Aprobado" if calificacion >= 8 else "Reprobado"
print(resultado)





