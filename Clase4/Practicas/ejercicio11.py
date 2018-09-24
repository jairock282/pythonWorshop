#Tasa de interes
agnos = 0
dolares = 0
tasa = 0


def capital(dola, ta, ag):

	a = (1 + (ta/100))

	capital = (dola * a )**ag

	print(capital)




print("Ingresa la cantidad de dolares")
dolares = int(input())

print("Ingresa una tasa de interes")
tasa = float(input())

print("Ingresa una cantidad de años")
agnos = int(input())

capital(dolares, tasa, agnos)
