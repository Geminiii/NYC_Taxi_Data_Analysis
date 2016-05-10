#!/usr/bin/env python
import sys

current_key = ""
current_trips = 0

for line in sys.stdin:
    key,value = line.strip().split('\t')
    if current_key == key:
        current_trips += 1
    else:
        if current_key != "":
            print "%s,%d" %(current_key,current_trips)
        current_key = key
        current_trips = 1
if current_key != "":
    print "%s,%d" %(current_key,current_trips)
