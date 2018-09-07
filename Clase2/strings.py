"""

La entrada de datos de los usuarios es de tipo String
el manejo y transformacion es muy importante

*Los Strings son inmutables, no se pueden cambiar o asignar valores

*split devuelve una lista
*join devuelve un string formado por los elementos de la lista

"""

"""
curso = "Curso de python"
tam = len(curso) #Tamaño del string
car = curso[2] #Caracter en un indice establecido pueden ser tambien indices negativos
sub = curso[1:15:2] #Crear subString

##No se pueden asignar o cambiar valores a un string
##curso[2] = "e"

print(curso)

print(tam)
print(car)
print(sub)
"""

##Realizar division del string
"""
lenguajes = "Python; java; c; c++; c++"

separador = ";"

##split divide el string, el caracter divisor predeterminado es el espacio -> lenguajes.split()
res = lenguajes.split(separador) ##Al dividirlo nos crea una lista con los elementos divididos

print(res)
"""

#Podemos crear de una lista un string con la funcion join
"""
lenguajes = "Python; java; c; c++; c++"
separador = ";"

res = lenguajes.split(separador)

nuevo_string = " ".join(res)
print(nuevo_string)
"""

##Realizar division de texto a traves de sus saltos de lines
texto = """Este es
un texto
de varias
lineas"""

resultado = texto.splitlines()
print(resultado) 

