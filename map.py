#!/usr/bin/python3
import sys

def mapper():
    for line in sys.stdin:
        fields = line.strip().split(';')

        if len(fields) >= 8:
            domain = fields[0].strip()
            file_type = fields[5].strip().split('.')[-1]
            bytes_str = fields[8].strip()

            if bytes_str.isdigit():
                print(f'{domain},{file_type}\t{bytes_str}')

if __name__ == "__main__":
    mapper()