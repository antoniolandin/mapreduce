#!/usr/bin/python3
import sys

def reducer():
    prev_hour = None
    prev_value = 0
    value = 0
    percentage = 0

    for line in sys.stdin:
        key , value_str = line.strip().split('\t')

        try:
            valueTotal = int(value_str)
        except ValueError:
            continue

        if prev_hour is None: 
            prev_hour = key

        if key == prev_hour:
            value += valueTotal
        else:
            if prev_value == 0:
                percentage = 0
            else:
                percentage = (value - prev_value) / (prev_value * 100) 

            print("Hour {:02d} incremento {:.6f}%".format(int(key), percentage))

            prev_hour = key
            prev_value = value
            value = valueTotal

    if prev_value == 0:
        percentage = 0
    else:
        percentage = (value - prev_value) / (prev_value * 100) 

    print("Hour {:02d} incremento {:.6f}%".format(int(key), percentage))


if __name__ == "__main__":
    reducer()