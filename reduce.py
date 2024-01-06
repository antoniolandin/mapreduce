#!/usr/bin/python3

import sys
from collections import defaultdict # porque me da error sin esta libreria ?????

def reducer():
    domains = defaultdict(int)

    for line in sys.stdin:
        key, value = line.strip().split('\t')
        domains[key] += int(value)

    top = sorted(domains.items(), key = lambda x: x[1], reverse = True)[:3]

    for domain, bytes in top:
        print(f'Dominio: "{domain}" - bytes: {bytes}')

if __name__ == "__main__":
    reducer()