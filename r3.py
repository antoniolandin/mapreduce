#!/usr/bin/python3


import sys

count = [0,0,0,0]

for line in sys.stdin:
	count[int(line)] += 1
	count[0] += 1

print("GET:"+str(count[1] /count[0])+" %")
print("POST:"+str(count[2] / count[0])+" %")
print("PUT:"+str(count[3] / count[0])+" %")