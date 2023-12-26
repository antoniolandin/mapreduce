#!/usr/bin/python3

import sys
 
for line in sys.stdin:    
    linea_limpia = line.strip()
    columnas = linea_limpia.split(";")

    if(len(columnas) == 9 and columnas[7] == "404"):
        
        if "." in columnas[5]:
            file_type = columnas[5].split(".")
            print(file_type[1])