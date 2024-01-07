#!/usr/bin/python3

import sys

primeraPeticion = True
total = 0
numBytesCache = 0 #Sirve para poder calcular la variación de la cantidad de bytes entre horas
aux = None

for line in sys.stdin:
    
    
    if(primeraPeticion):
        aux ,numBytes = line.strip().split('\t')
        primeraPeticion = False
        hora = aux
    else:
        hora ,numBytes  = line.strip().split('\t')

    #Para calcular la variación de bytes, necesitamos la diferencia entre los bytes actuales y anteriores
    #numBytes-> bytes actuales
    #numBytesCache-> bytes de la acción anterior
    #variación -> ( (actuales - anteriores) / anteriores )

    #Al inicio no hay valores anteriores con los que comparar, asi que no hay variacion -> 0

    if(aux != hora):
        if(numBytesCache == 0):
            print("HORA: "+str(aux)+" Variación: 0")
        else:
            variacion = float(((total - numBytesCache)/numBytesCache*100)) #Si multiplicamos por 100 conseguiremos el %
            print(f'HORA: {aux} Variación: {variacion:.4f}%')
        numBytesCache = total
    else:
        total += int(numBytes)
    aux = hora
     #almacenamos los bytes para poder compararlos con los siguientes

variacion = float(((total - numBytesCache)/numBytesCache*100)) #Si multiplicamos por 100 conseguiremos el %

print(f'HORA: {aux} Variación: {variacion:.4f}%')