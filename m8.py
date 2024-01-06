#!/usr/bin/python3
import sys
import os

for line in sys.stdin:
    columnas = line.strip().split(';')

    if len(columnas) >= 8:
        dominio = columnas[0]

        #Obtenemos extension del archivo
        extension = os.path.splitext(columnas[5])       #Le quitamos el punto a la extension del archivo
        extension_limpia = extension[-1].strip().lstrip(".")
        #Filtro que solo admite enteros
        if(columnas[8].isdigit()):
            numBytes = int(columnas[8].strip())
            print(f'{dominio}\t{numBytes}\t{extension_limpia}')
