print("Cantidad de segundos en un lustro\n")

##Planteamos la cantidad de segundos por agno
seg_hora = int(3600)
seg_dia = int(3600*24)
seg_agno = int(seg_dia * 365)
seg_bisiesto = int(seg_dia * 366)

##Procedimiento

##Sumamos la cantidad de segundos que hay en 4 años con 365 y lo de un año bisiesto
seg_lustro = int((seg_agno * 4) + seg_bisiesto)
print(seg_lustro,"segundos")
