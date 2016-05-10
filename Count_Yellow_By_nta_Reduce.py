#!/usr/bin/env python
import sys

current_key = ""
current_57trips = 0
current_810trips = 0

for line in sys.stdin:
    key,value = line.strip().split('\t')
    month,trips = value.split(',')
    month = int(month)
    trips = int(trips)
    if current_key == key:
        if month>=5 and month<=7:
            current_57trips += trips
        else:
            current_810trips += trips
    else:
        if current_key != "":
            print "%s\tyellow,%d,%d" %(current_key,current_57trips,current_810trips)
        current_key = key
        if month>=5 and month<=7:
            current_57trips = trips
            current_810trips = 0
        else:
            current_810trips = trips
            current_57trips = 0
if current_key != "":
            print "%s\tyellow,%d,%d" %(current_key,current_57trips,current_810trips)
