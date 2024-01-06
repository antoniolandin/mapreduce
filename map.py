#!/usr/bin/python3

import sys

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def mapper():
    for line in sys.stdin:
        fields = line.strip().split(';')
        if len(fields) >= 8 and is_numeric(fields[7]): 
            print(f'{fields[4]}\t{fields[7][0]}')

if __name__ == "__main__":
    mapper()