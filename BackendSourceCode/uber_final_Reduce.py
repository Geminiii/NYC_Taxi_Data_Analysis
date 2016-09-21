#!/usr/bin/env python
import sys

current_key = ""
current_uber = 0
current_total = 0

for line in sys.stdin:
    key,value = line.strip().split('\t')
    car,trips = value.split(',')
    trips = int(trips)
    if current_key == key:
        if car=="uber":
            current_uber += trips
        current_total += trips
    else:
        if current_key != "":
            result = 0.0558 - float(current_uber)/float(current_total)
            print "%s,%f" %(current_key,result)
        current_key = key
        if car=="uber":
            current_uber = trips
        else:
            current_uber = 0
        current_total = trips
if current_key!= "":
    result = 0.0558 - float(current_uber)/float(current_total)
    print "%s,%f" %(current_key,result)
