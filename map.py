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

        if len(fields) >= 9:
            try:
                if is_numeric(fields[7]): 
                    print(fields[4],"\t", fields[8]) # output
            except (ValueError, IndexError):
                continue

if __name__ == "__main__":
    mapper()