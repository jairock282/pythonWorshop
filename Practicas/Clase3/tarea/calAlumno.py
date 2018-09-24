#Diccionario calificaciones alumno

#calificacioes
calificaciones = {"calculo":10, "dibujo":5}
#Realizamos lista los value del diccionario
listCalif = list(calificaciones.values())
sumaCalif = 0
promedio = 0

#Recorremos la lista de calificaciones y realizamos sumatoria
num = len(listCalif)
for i in range(num):

	sumaCalif += listCalif[i] 

#Obtenemos promedio
promedio = sumaCalif / num

#imprimimos promedio
print(promedio)
