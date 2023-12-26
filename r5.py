#!/usr/bin/python3


import sys

file_type = []

for line in sys.stdin:

    linea_limpia = line.strip()

    if linea_limpia not in file_type:
        
        file_type.append(linea_limpia)

print(file_type)