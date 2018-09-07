##Para crear matrices se necesita hacer listas anidadas
"""
matriz = [10][20]
         [30][40]
"""

fila_uno = [10, 20]
fila_dos = [30, 40]

##Anidamos las listas
matriz = [fila_uno, fila_dos]

primer_elemento = matriz[0][0]

print(primer_elemento)
