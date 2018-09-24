##Numeros binarios a enteros

binario = [1,1,0,1,0,1]
biFlip = []

tam = len(binario)

def flip_bi():

	for i in range(tam, 0, -1):
		biFlip.append(binario[i-1])



def get_Deci():

	flip_bi()
	decimal = 0;

	for i in range(0, tam, 1):

		if (biFlip[i] != 0):

			decimal = decimal + 2**(biFlip[i]*i)
		else:
			decimal = decimal + 0

	print("Decimal -> ", decimal)


get_Deci()
