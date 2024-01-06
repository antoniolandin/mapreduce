#!/usr/bin/python3

import sys

aux = None
count = 0
total = 0
primeraPeticion = True

for line in sys.stdin:
	
	#Hacemos que no sea None la primera peticion
	if(primeraPeticion):  
		aux = line.strip()
		peticion = aux
		primeraPeticion = False
	else:
		peticion = line.strip()
	
	if(aux != peticion):
		total += count
		print(str(aux)+" %: "+ str(count/total))
		count = 0
	else:
		count += 1
	aux = peticion
print(str(aux)+" %: "+ str(count/total))