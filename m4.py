#!/usr/bin/python3

import sys


for line in sys.stdin:
    columnas = line.strip().split(";")

    if(len(columnas) >= 8):
        tipoRespuesta = columnas[7][0]  #Necesitamos solo el primer número para saber el tipo de respuesta
        #Filtramos para que el tipo de la respuesta se un número y no una letra
        if(tipoRespuesta.isdigit()):
            print(columnas[4]+" "+tipoRespuesta)