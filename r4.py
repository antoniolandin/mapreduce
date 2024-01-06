#!/usr/bin/python3

import sys

aux = None
count = 0
primeraPeticion = True

for line in sys.stdin:

	#Hacemos que no sea None la primera peticion
    if(primeraPeticion):
        aux = line.strip().split(' ')
        primeraPeticion = False
        peticion = aux
    else:
        peticion = line.strip().split(' ') 
    #peticion[0]-> tipo peticion 
    #peticion[1]-> tipo de respuesta
    if((aux[0] != peticion[0]) or (aux[1] != peticion[1])):
        print(str(aux[0])+" "+str(aux[1])+"XX: "+str(count))
        count = 1
    else:
        count += 1
    aux = peticion
print(str(aux[0])+" "+str(aux[1])+"XX: "+str(count))