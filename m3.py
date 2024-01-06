#!/usr/bin/python3

import sys


for line in sys.stdin:    
    columnas = line.strip().split(";")

    if(len(columnas) >= 8):
        print(columnas[4])
        