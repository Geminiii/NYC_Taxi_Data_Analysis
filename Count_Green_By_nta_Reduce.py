#!/usr/bin/env python
import sys

current_key = ""
current_trips = 0

for line in sys.stdin:
    key,value = line.strip().split('\t')
    month,trips = value.split(',')
    trips = int(trips)
    if current_key == key:
        current_trips += trips
    else:
        if current_key != "":
            print "%s\tgreen,0,%d" %(current_key,current_trips)
        current_key = key
        current_trips = trips
if current_key != "":
    print "%s\tgreen,0,%d" %(current_key,current_trips)
