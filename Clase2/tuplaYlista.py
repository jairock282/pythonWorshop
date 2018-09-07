#tupla = (1, 2, 3, 4, 5, 6)
#lista = [10, 20, 30, 40]
#tupla_dos = (100, 200, 300, 400)

"""
##Tupla que contiene tuplas
resultado = zip(tupla, lista)
##Si no casteamos nos dara una direccion de memoria
resultado = tuple(resultado)
"""
"""
##Lista que contiene tuplas
resultado = zip(tupla, lista)
##Si no casteamos nos dara una direccion de memoria
resultado = list(resultado)
"""
"""
##Lista que contiene tuplas
resultado = zip(tupla, lista, tupla_dos)
##Si no casteamos nos dara una direccion de memoria
resultado = list(resultado)
"""

"""
##Convertir de duplas a listas
lista = ["Python", "java", "c", "c++"]
tupla = ("Introduccion", "tuplas", "listas")
##De tupla a lista
nueva_lista = list(tupla)
##De lista a tupla
nueva_tupla = tuple(lista)

print(nueva_lista)
"""
###-----------------------------------------------

##Convertir de un string a una tupla o a lista
mensaje = "Estoy en el taller de Python Basico"

##Se agregaran los caracteres incluyendo los espacios
tupla = tuple(mensaje)
lista = list(mensaje)

print(tupla)
print(lista)
