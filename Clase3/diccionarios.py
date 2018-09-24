"""
nomDic.get("key", "impresion de algo") -> verificar existencia

nomDic.setDefault("key", valor default) -> definir valor predeterminado

nomDic.key() -> devuelve todas las llaves

nomDic.values() -> devuelven los valores de las llaves

"""
##Creamos una estructura diccionario

##Lo que va dentro de la llave puede ser cualquier tipo de dato inmutable (String, int, etc)

##Creamos una llave "nomllave":valor
diccionario = {"total":55, "descuento":15, "recargos":"no aplica"}

##Acceder a valor dentro del diccionario
diccionario["total"] = 100
valor = diccionario["descuento"]

##Verificamos que la llave exista en el diccionario
#resultado = "z" in diccionario
#print(resultado)

#Podemos agregar una frase que se imprima dependiendo de la situacion de la
#llave
print(diccionario.get("z", "La llave z no existe"))


#Podemos definir un valor predeterminado a la llave si es
#que no tiene ninguno asignado
resultado = diccionario.setdefault("d", [])
print(resultado)


#Obtenemos la cantidad de llaves que existen en el diccionario
numLlaves = diccionario.key()
numLlaves = tuple( numLlaves )
print(numLlaves)

#Obtenemos los valoes de las distintas key
valores = diccionario.values()
valores = list(valores)
print(valores)

#Obtener todas las llaves y valores del diccionario
allItem = diccionario.items()
allItem = list(allItem)
print(allItem)


#Contados de elementos en el diccionario
print(len(diccionario))

#Borrar elementos del diccionario
	del diccionario["a"]
	print(len(diccionario))
	print(diccionario)

	##opcion 2
	diccionario.pop("b")
	print(len(diccionario))

#AL momento de borrar podemos guardar el valor de la llave
#	valor = diccionario.pop("b")

#Borrar todos los elementos del diccionario

	diccionario.clear()
	print(diccionario)

#El valor none, representa la ausencia de valor y/o false

print(valor)


