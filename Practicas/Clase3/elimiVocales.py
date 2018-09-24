##Cantidad de vocales

#Declaramos nuestras listas y variables necesarias
lista = []
numVoca = 0

#El string que se ingresa lo casteamos a lista y separamos cada caracter
print("Ingresa tu frase")
string = input()
string = string.split()
#print(string)
newstring = "".join(string)
#print(newstring)
newstring = newstring.lower()
newstring = list(newstring)

#print(lista)

largoString = len(newstring)

for i in range(largoString):

	if (newstring[i] == 'a') or (newstring[i] == 'e') or (newstring[i] == 'i') or (newstring[i] == 'o') or (newstring[i] == 'u'):

                newstring[i] = ""


sinVC = "".join(newstring)

print("String sin vocales -> ", sinVC)
