#!/usr/bin/python3
import sys

for line in sys.stdin:
    columnas = line.strip().split(';')

    if len(columnas) >= 8:
        
        dominio = columnas[0]
        #Filtro que solo admite enteros
        if(columnas[8].isdigit()):
            bytes = int(columnas[8].strip())  #Lo transformamos en int
            print(f'{dominio}\t{bytes}')
