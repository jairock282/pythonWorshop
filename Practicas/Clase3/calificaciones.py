##Promedios Calificaciones desde un diccionario

calificaciones = {"calculo":10, "algebra":9, "circuitos":10}

listValores = list(calificaciones.values())
suma = 0

for value in listValores:

	suma += value


print("El promedio es: ", suma / len(listValores))
print("La materia con mejor promedio es: ",)
