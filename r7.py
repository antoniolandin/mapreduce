#!/usr/bin/python3

#Información sobre la función que ordena diccionarios por valor
# https://geekflare.com/es/python-dictionary-sorting/

from collections import defaultdict
import sys
primerDominio = True

aux = None
diccionario = defaultdict(int)   #En el diccionario almacenaremos los nombres de los dominios y los bytes totales

for line in sys.stdin: 
    aux, numBytes = line.strip().split('\t')

    #Sumamos al diccionario los bytes correspondientes a su key
    diccionario[aux] += int(numBytes)       #No se porqué no detectaba que le he pasado int 

diccionario_ordenado = sorted(diccionario.items(),key=lambda item:item[1], reverse=True)

#Imprimimos solo los 3 primeros
for i in range(3):
    print(diccionario_ordenado[i])
