##Operadores realciones y logico

valor_uno = 10
valor_dos = 18

##Operadores relacionales: evaluan valores numericos y resulta un valor booleano
mayor = valor_uno > valor_dos #False
menor = valor_uno < valor_dos #True
mayor_igual = valor_uno >= valor_dos #False
menor_igual = valor_uno <= valor_dos #True
##igual = valor_uno == valor_dos #False

##En Python podemos utilizar la palabra reservada is
igual = valor_uno is valor_dos #False
diferente = valor_uno != valor_dos #True

"""
print(mayor)
print(menor)
print(mayor_igual)
print(menor_igual)
print(igual)
print(diferente)

"""

print("Estas autorizado? si/no")
autorizacion = input() == "si"
print(autorizacion)
