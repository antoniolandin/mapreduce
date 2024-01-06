#!/usr/bin/python3

import sys

aux = None
count = 1

for line in sys.stdin:
	
	peticion = line.strip()
	
	if(aux != peticion):
		print(str(aux)+" Count: "+str(count))
		count = 0
	count += 1
	aux = peticion
print(str(aux)+" Count: "+str(count))
