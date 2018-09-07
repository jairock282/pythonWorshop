##Cuando creamos una dupla los elemento se definen entre parentesis
##Son mas rapidos al momento de obtener los elementos que las listas

"""
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

##Obtener un elemento en especifico
elemento = tupla[4]

##Tambien maneja indices negativos
elemento = tupla[-1]

##Se pueden crear subTuplas
subTupla = tupla[:9:2]
"""

#---------------Descomprimir elementos----------
"""
##Asiganar los valores de la tupla a varibles que si pueden ser modificas
tupla = (1, 2, 3, 4)

##Se asignan los valores
##uno, dos, tres, cuatro = tupla[0], tupla[1], tupla[2], tupla[3]

##Tambien se puede realizar de manera mas corta, es necesario definir ua variable por cada elemento de la tupla
uno, dos, tres, cuatro = tupla
"""
###

"""
##Podemos definir mas de un elemento a una variable en forma de lista
tupla = (1, 2, 3, 4, 5, 6)

uno, dos, tres, *cuatro = tupla
"""


##Podemos combinar las formas de asignacion
tupla = (1, 2, 3, 4, 5, 6)

uno, *dos,cinco, seis = tupla 

print(tupla)

print(uno)
print(dos)
print(cinco)
print(seis)


