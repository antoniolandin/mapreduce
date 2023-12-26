#!/usr/bin/python3


import sys

count = [0,0,0]

for line in sys.stdin:
	count[int(line)] += 1

print("GET:"+str(count[0]))
print("POST:"+str(count[1]))
print("PUT:"+str(count[2]))
#SE PUEDEN AÑADIR LAS PETICIONES QUE SE DESEEN