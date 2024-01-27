#!/usr/bin/python3

import sys
import heapq

def top3Heap(heap, countBytes, dominio, extension):
    # comprobamos si el heap tiene menos de 3 elementos
    if(len(heap) < 3):
        heapq.heappush(heap, (countBytes, dominio, extension))
    else:
        # comprobamos si el elemento que queremos insertar es mayor que el menor del heap
        if(countBytes > heap[0][0]):
            heapq.heappushpop(heap, (countBytes, dominio, extension))

aux = None
dominioAux = None
heap = []
countBytes = 0

for line in sys.stdin: 

    try:
        dominio, numBytes, extension = line.strip().split('\t')    #Si el separador no es \t no funciona

        if(aux == None and dominioAux == None):
            countBytes = int(numBytes)
        elif(aux != dominio or dominioAux != dominio):
            top3Heap(heap, countBytes, dominio, extension)
            countBytes = 0
        else:
            countBytes += int(numBytes)

        aux = dominio
        dominioAux = dominio

    except:
        pass

for i in heap[::-1]:
    print(i[1] + '\t' + str(i[0]) + '\t' + i[2])
