#!/usr/bin/env python
import sys

current_key = ""
current_trips = 0
current_revenue = 0

for line in sys.stdin:
    key,value = line.strip().split('\t')
    trips,revenue = value.split(',')
    try:
        trips = int(trips)
        revenue = float(revenue)
    except ValueError:
        continue
    if current_key == key:
        current_trips += trips
        current_revenue += revenue
    else:
        if current_key != "":
            areaid,month = current_key.split(',')
            print "%s\t%s,%d,%f" %(areaid,month,current_trips,current_revenue)
        current_key = key
        current_trips = trips
        current_revenue = revenue
if current_key != "":
    areaid,month = current_key.split(',')
    print "%s\t%s,%d,%f" %(areaid,month,current_trips,current_revenue)
