"""
.capitaliza() cambiar la primera a mayuscula
.swapcase() cambiar las mayus a minus y al contrario
.upper() cambiar todas a mayus
.lower() cambiar todas a minus
.isupper() verificar si estan en mayus
.islower() verificar si estan en minus
.title() determinar que ese string es un titutlo

"""
texto = "curso de Python Basico"

##Cambio de la primera letra del string a mayus
"""
res = texto.capitalize()
print(res)

"""
##Cambio de mayus a minus
"""
res = texto.swapcase()
print(res)

"""
##Cambiar todas a mayusculas
"""
res = texto.upper()
print(res)

"""

##Cambiar todas a minusculas
"""
res = texto.lower()
print(res)

"""
#Verificar si todas estan en minus o mayus
"""
res = texto.lower()
print(res.islower())
"""

##Remplazar alguna palabra en el nuevo string que se esta creando, se le puede determinar cuantas veces se dee realizar el cambio
"""
res = texto.remplace("Python", "Django", 1)
print(res)
"""

##Manter espacio determinados
"""
texto1 = "    Curso de python   "
res = texto1.strip()
print(texto)
print(res)
"""

##Combinar strings
"""
curso = "Python"
horario = "Viernes de 9 a 13"
#resultado = "Curso de %s %s" %(curso, horario)
#resultado = "Curso de {} {}".format(curso, horario)

##Podemos colocar identificadores para establecer el orden
resultado = "Curso de {a} {b}".format(b=horario, a=curso)

print(resultado)
"""

##Todo lo que se cocatene en el string dara como resultado otro string
"""
curso = "Curso de Python basico"

##Estamos sobre escribiendo la variable
##curso = "c" + curso[1:] + " en la Facu de info"

curso = "c" + curso[1:] + " con "+ str(20) +" alumnos"

print(curso)
"""


##Busqueda de caracteres dentro de cadenas de texto
mensaje = "Este es un mensaje en cuanto de varios caracteres"

#res = mensaje.count("mensaje") #Cuantas veces aparece la palabra

#res = "mensaje" in mensaje #Se encuentra la palabra

#res = "mensaje" not in mensaje #No se encuentra

#res = mensaje.find("mensaje") #El indice en donde comienza la palabra mensaje

#res = mensaje[11 : 11+len("mensaje")] #Estamos realizando una subcadena de caractares

#res = mensaje.startswith("este") #Ver con que caracter o palabra comienza, es sensible a mayus y minus

res = mensaje.endswith(".") #Ver con que caracter o palabra termina, es sensible a mayus y minus

print(res)
