#!/usr/bin/python3

import sys


for line in sys.stdin:    
    columnas = line.split(";")

   
    if(len(columnas) > 4 and columnas[4] == "GET"):
        print(0)
    if(len(columnas) > 4 and columnas[4] == "POST"):
        print(1)
    if(len(columnas) > 4 and columnas[4] == "PUT"):
        print(2)
          