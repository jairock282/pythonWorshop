##Los elementos de una lista se define entre corchetes
lenguajes = ["Python", "C", "C++", "C#", "Django", "r", "java"]

##Se puede imprimir las posiciones asignando su lugar de 0 - (n-1)
##resultado = lenguajes[2]

##Tambien se puede acceder a las posiciones en orden inverso
##resultado = lenguajes[-1]

##Se pueden crear intervalos de impresion dato1:dato2
##resultado = lenguajes[0:3]

##si queremos imprimir desde el 0, no es necesario definirlo :dato2
##resultado = lenguajes[:3]


##Si queremos que termine de imprimir todo desde un punto inicial, solo lo determinamos dato1:
##resultado = lenguajes[2:]


##Podemos imprimir todo :
##resultado = lenguajes[:]

##Podemos definir rangos y ademas su intervalo de salto [dato1:dato2:intervalo]
##resultado = lenguajes[1:7:2]


##Imprimir la lista en orden inverso
##resultado = lenguajes[ : :-1]



#----------------------------------------------------------------------------------------

#------------------OPERADORES-------------------------

lista = [8.17, 90, 1, 5, 5, 44, 1.32]

#Aplicamos el algoritmo de ordenamiento Sort, lo ordena de manera ascendente
##lista.sort()

##Aplicar algoritmo sort y ordena de manera descendente
lista.sort(reverse = True)

print(lista)


menor = min(lista) # Devuelve el numero menor de la lista

mayor = max(lista) # Devuelve el numero mayor de la lista

longitud = len(lista) # Devuelve el numero de elementos de la lista

resultado =  8 in lista #Devuelve si el elemento se encuentra en la lista puede ser con is

index = lista.index(8.17) #Me duelve el index de determinado elemento

contador = lista.count(5) # Me devuelve cuantos elementos iguales hay


print(menor)
print(mayor)
print(longitud)
print(resultado)
print(index)
print(contador)
