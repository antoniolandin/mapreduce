#!/usr/bin/python3

import sys
from collections import defaultdict

def reducer():
    filetype_bytes = defaultdict(int)

    for line in sys.stdin:
        key, value = line.strip().split('\t')
        domain, file_type = key.split(',')
        bytes = int(value)

        filetype_bytes[file_type] += bytes

    top_filetypes = sorted(filetype_bytes.items(), key=lambda x: x[1], reverse=True)[:3]
    for file_type, bytes in top_filetypes:
        print(f'Tipo de archivo: {file_type} {bytes}')

if __name__ == "__main__":
    reducer()