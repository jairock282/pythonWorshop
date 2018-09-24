#es_bisiesto

def es_bisiesto():

	print("Ingrese el año a verificar")
	agno = int(input())

	if (agno%4 == 0) and (agno%100 != 0):

		if(agno/400):

			print("Es bisiesto!")
	else:

		print("No es bisiesto")


es_bisiesto()
