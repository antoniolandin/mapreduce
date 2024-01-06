#!/usr/bin/python3

import sys
import os   #Hay una función que nos permite obtener la extensión facilmente
            #os.path.splitext("nombre")
            #información sacada de StackOverflow
            #> https://es.stackoverflow.com/questions/562647/cómo-crear-una-lista-de-paths-de-archivos-filtrados-por-su-extensión-jpg-en-un-á

hora = '10'

for line in sys.stdin:
    columnas = line.strip().split(';')

    if ((len(columnas) >= 8) and (columnas[7] == '404')):
        #Para obtener el campo donde está la hora, miramos columnas[3]
        #En ese campo hacemos un split para obtener la fecha y hora
        campoTiempo = columnas[3].strip().split(' ')

        #tiempo -> fecha - hora
        # hora ->  horas:minutos:segundos
        campoHora = campoTiempo[1].split(':')
        if(campoHora[0] == hora):
            extension = os.path.splitext(columnas[5])
            print(extension[-1])