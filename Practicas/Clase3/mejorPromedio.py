##Promedios Calificaciones desde un diccionario

calificaciones = {"calculo":10, "algebra":9, "circuitos":10}

listValores = list(calificaciones.values())
listaMaterias = list(calificaciones.keys())
suma = 0

##Buscamos la calificacion mas alta
maxCalif = max(listValores)
##Obtenemos el index de la calificacion mas alta
indexMax = listValores.index(maxCalif)
##Obtenemos la materia con la calif mas alta
materiaSuprema = listaMaterias[indexMax]


for value in listValores:

        suma += value

print("El promedio es: ", suma / len(listValores))
print("La materia con el promedio mas alto es: ", materiaSuprema)
