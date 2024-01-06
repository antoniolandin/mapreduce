#!/usr/bin/python3
import sys

def mapper():
    for line in sys.stdin:
        fields = line.strip().split(';')

        if len(fields) >= 8:
            try: 
                domain = fields[0]
                bytes = int(fields[8].strip())
                print(f'{domain}\t{bytes}')
            except ValueError:
                continue
            
if __name__ == "__main__":
    mapper()