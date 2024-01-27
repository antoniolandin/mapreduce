#!/usr/bin/python3

import heapq
import sys

def top3Heap(heap, peticion, count):
    # comprobamos si el heap tiene menos de 3 elementos
    if(len(heap) < 3):
        heapq.heappush(heap, (count, peticion))
    else:
        # comprobamos si el elemento que queremos insertar es mayor que el menor del heap
        if(count > heap[0][0]):
            heapq.heappushpop(heap, (count, peticion))

aux = None
heap = []
countBytes = 0

for line in sys.stdin: 
    peticion, numBytes = line.strip().split("\t")

    if(aux == None):
        aux = peticion
        countBytes = int(numBytes)
    elif(aux != peticion):
        top3Heap(heap, aux, countBytes)
        countBytes = 0
    else:
        countBytes += int(numBytes) 

    aux = peticion

for i in heap[::-1]:
    print(i[1] + "\t" + str(i[0]))
