#!/usr/bin/python3
import sys

for line in sys.stdin:
    columnas = line.strip().split(';')
        
    if len(columnas) >= 8:
        campoTiempo = columnas[3].strip().split(' ')
        campoHora = campoTiempo[1].split(':')
        if(columnas[8].isdigit()):   
            print(f'{campoHora[0]}\t{columnas[8]}')  #Ponemos primero la hora para que el sort ordene correctamente