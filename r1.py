#!/home/antonio/.anaconda3/bin/python

import sys

count = 0

for line in sys.stdin:
	count  += 1

print(count)