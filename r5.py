#!/usr/bin/python3

import sys

aux = None  #Auxiliar de control

for line in sys.stdin: 
    extension = line.strip().lstrip(".")
    #Podemos utilizar una única variable temporal para agrupar todo
    if (aux != extension):
        print(aux)
    aux = extension