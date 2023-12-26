#!/usr/bin/python3

import sys
 
for line in sys.stdin:    
    columnas = line.split(";")
       
    if(len(columnas) > 4 and columnas[4] == "GET"):
            print(1)
    
    
 
    