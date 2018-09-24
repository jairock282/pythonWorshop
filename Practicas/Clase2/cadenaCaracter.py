"""
#Ingresamos la cadena de Caracteres
#A)
print("Caracteres separados\n")
##Pedimos la cadena de caracteres y el separador
print("Ingrese una cadena de caracteres")
cadena = input()
print("Ingrese caracter separador")
separador = input()

##El string lo convertimos a lista para obtener cada palabra
cadaCaracter = list(cadena)
#print(cadaCaracter)

##Creamos un nuevo string insertando el separador definido entre caracteres
newString = separador.join(cadaCaracter)
print(newString)



#B)
print("\nPalabras separadas\n")
##Pedimos la cadena de caracteres y el separador
print("Ingrese una cadena de caracteres")
cadena = input()
print("Ingrese caracter separador")
separador = input()

##El string lo convertimos a lista para obtener cada palabra
cadaPalabra = cadena.split()
#print(cadaPalabra)


##Creamos un nuevo string insertando el separador definido entre caracteres
newString = separador.join(cadaPalabra)
print(newString)


#C)
print("\nRemplazo de caracteres\n")
print("Ingrese una cadena de caracteres")
cadena = input()
print("Ingrese caracter de sustitucion")
susti = input()

##El string lo convertimos a lista para obtener cada palabra
cadCaract = list(cadena)

for i in range(len(cadCaract)):
	cadCaract[i] = susti

newString = "".join(cadCaract)
print(newString)
"""
#D)
print("\nCada tres caracteres\n")
print("Ingrese una cadena de caracteres")
cadena = input()

cadaCarac = list(cadena)
cada3 = cadaCarac[::3]

newString = ".".join(cada3)
print(newString)

