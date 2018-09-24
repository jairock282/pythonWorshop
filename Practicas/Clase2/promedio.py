#Formato entrada datos
	#nombreAlumno_Calificacion1_Calificacion2_Calificacion3

#Entrada teclado
print("Siga la siguiente estructura nombre Alumno_Calif1_Calif2_Calif3")
calAlumno = input()
#calAlumno = "Jaime_10_9_8"
separador = "_"

res = calAlumno.split(separador)

calif1 = 0
calif2 = 0
calif3 = 0
sumProm = 0
promedio = 0

nomAlumno = res[0]
calif1 = int(res[1])
calif2 = int(res[2])
calif3 = int(res[3])

sumProm = calif1 + calif2 + calif3
promedio = sumProm / (len(res) - 1)

print("Nombre del alumno: ", nomAlumno)
print("Calificación1: ", calif1)
print("Calificación2: ", calif2)
print("Calificación3: ", calif3)
print("Promedio: ", promedio)
