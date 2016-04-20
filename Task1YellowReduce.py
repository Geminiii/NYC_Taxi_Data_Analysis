#!/usr/bin/python
import sys

current_key = ""
current_trips = 0
current_revenue = 0

for line in sys.stdin:
    key,revenue = line.strip().split('\t')
    try:
        revenue = float(revenue)
    except ValueError:
        continue
    if current_key == key:
        current_trips += 1
        current_revenue += revenue
    else:
        if current_key != "":
            zipcode,month = current_key.split(',')
            print "%s\t%s,%d,%f" %(zipcode,month,current_trips,current_revenue)
        current_key = key
        current_trips = 1
        current_revenue = revenue
if current_key != "":
    zipcode,month = current_key.split(',')
    print "%s\t%s,%d,%f" %(zipcode,month,current_trips,current_revenue)
