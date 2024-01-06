#!/usr/bin/python3
import sys

for line in sys.stdin:
    columnas = line.strip().split(';')

    if len(columnas) >= 8:
        dominio = columnas[0]
        
        #Filtro que solo admite enteros
        if(columnas[8].isdigit()):
            numBytes = int(columnas[8].strip())    #Lo transformamos en int

            print(f'{dominio}\t{numBytes}')        #Si el separador no es \t no funciona
