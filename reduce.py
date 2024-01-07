#!/usr/bin/python3
import sys

def reducer():
    temp=['GET']
    i=0
    cantidadPet=1
    bitsGet = balance = 0
    
    for line in sys.stdin:
        key, value= line.strip().split('\t')

        value = value.strip()
        value = value.rstrip('s')
        
        if(temp==key):
            value=int(value)
            i=value+i
        else:
            if i != 0 and cantidadPet != 0:
                bitsGet = i/1
                print(f"Media bits por peticion {temp}: {i/1}")
            i=0
            temp=key
    if i != 0 and cantidadPet != 0:
        print(f"Media bits por peticion {temp}: {i/1}")
        balance = bitsGet - i/1
        print(f"Balance de bits: {balance}")

if __name__ == "__main__":
    reducer()