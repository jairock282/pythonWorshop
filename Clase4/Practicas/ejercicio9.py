##Master Mind

from random import *

list = []

def fill_list(num):

	for i in range(num):

		list.append(randint(1,9))

#	print("Se relleno la lista")
#	print(list)

	return list

def igual(randomList, lista, num):

	cont = 0

	for i in range(0, len(lista), 1):

		if (randomList[i] == lista[i]):

			cont = cont + 1
	if (cont == len(lista)):

		print("Con ",num," has adivinado ", cont, " valores. Felicidades!")

	else:

		print("Con ",num," has adivinado ", cont, " valores")

	return cont



def intento(lista):

	listIntento = []

	print("Intenta adivinar la cadena:")
	num = input()

	for i in range(len(num)):

		listIntento.append(int(num[i]))


	adivino = igual(lista, listIntento, num)

	return adivino

def master_mind():

	ad = 0

	print("Dime la longitud de la cadena: ")
	long = int(input())

	while(ad != long):

		ad = intento(fill_list(long))


master_mind()
