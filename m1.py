#!/home/antonio/.anaconda3/bin/python

import sys
 
lineas_filtradas = []
 
for line in sys.stdin:    
    columnas = line.split(";")
       
    if(len(columnas) > 4 and columnas[4] == "GET"):
            print(1)
    
    
 
    