#Damos la entrada
print("Ingrese la entrada con ;")
entrada = input()

separador = ";"

res = entrada.split(separador)

print("ID:",res[0])
print("Name:",res[1])
print("Country:",res[2])
print("Avarage:",res[3])
print("Board type:",res[4])
print("Age:",res[5])

