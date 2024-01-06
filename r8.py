#!/usr/bin/python3

#Información sobre la función que ordena diccionarios por valor
# https://geekflare.com/es/python-dictionary-sorting/

from collections import defaultdict
import sys

aux = None
diccionario = defaultdict(int)  

for line in sys.stdin: 
    try:
        aux, numBytes, extension = line.strip().split('\t')    #Si el separador no es \t no funciona
        diccionario[extension] += int(numBytes)
    except ValueError:
        continue  

diccionario_ordenado = sorted(diccionario.items(),key=lambda item:item[1], reverse=True)

for i in range(3):
    print(diccionario_ordenado[i])