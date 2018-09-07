"""
print("Que onda que pex, ingresa tu nombre ")
##Entrada por teclado
nombre = input()
print("Bienvenido ", nombre, ". Ingresa tu edad: ")
##Todas la entradas por teclado ingresan como cadenas de caracteres, por lo
##que se tiene que definir si es algun tipo diferente de dato
edad = int(input())
print("En diez años tendras ", edad+10)
print("No quiero ser chismoso pero, cual es tu peso?")
peso = float(input())
print("El peso es de ", peso)

"""

##Para evitar el print en los datos ingresados desde teclado se coloca dentro de la misma funcion de input

nombre = input("Que onda que pex, ingresa tu nombre \n")

edad = int(input("Ingresa tu edad: "))
print("En diez años tendras ", edad+10)

peso = float(input("No quiero ser chismoso pero, cual es tu peso? "))
print("El peso es de ", peso)


