#Asignamos valor a la variable
cadena = "esto es un ejemplo"

#Realizamos una lista indicando que el separador es un espacio
listCadena = cadena.split(" ")

#Realizamos dos sublistas
sub1 = listCadena[2: :1]
sub2 = listCadena[1::-1]

#Juntamos las dos listas
newList = sub1 + sub2

#Creamos nuestro nuevo string
newString = " ".join(newList)

#print(listCadena)
#print(sub1)
#print(sub2)
#print (newList)


print(newString)
