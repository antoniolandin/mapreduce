#!/usr/bin/python3

import sys

peticion = None
aux = None
count = 0
totalNumBytes = 0
i = 0
primeraPeticion = True
avg = [0,0]

for line in sys.stdin: 

    if(primeraPeticion):  
	    aux, numBytes = line.strip().split('\t')
	    peticion = aux
	    primeraPeticion = False
    else:
        peticion, numBytes = line.strip().split('\t')
    

    #Balance -> AVG(GET) - AVG(POST)
    #i-> cuando se cambia de petición, aumenta la i
    if(aux != peticion):
        avg[i] = int(totalNumBytes)/int(count)
        totalNumBytes = 0
        count = 0
        i += 1
    else:
        totalNumBytes += int(numBytes)
        count += 1
    aux = peticion
    
avg[i] = int(totalNumBytes)/int(count)

print("AVG de bits petición GET: "+ str(avg[0]))
print("AVG de bits petición POST: "+ str(avg[1]))
print("Balance de trafico: "+ str(avg[0]-avg[1]))

