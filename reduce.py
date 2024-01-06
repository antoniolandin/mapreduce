#!/usr/bin/python3

import sys
from collections import defaultdict

def reducer():
    counts = defaultdict(int)
    for line in sys.stdin:
        key, value = line.strip().split('\t')
        counts[key + ' ' + value + 'XX'] += 1

    for key, count in counts.items():
        print(f"{key}: {count}")

if __name__ == "__main__":
    reducer()