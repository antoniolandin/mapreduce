#!/usr/bin/python3
import sys
import os

for line in sys.stdin:
    columnas = line.strip().split(';')

    if len(columnas) >= 8 and (columnas[4] == "GET" or columnas[4] == "POST"):
        if(columnas[8].isdigit()):
            print(f'{columnas[4]}\t{columnas[8]}')
