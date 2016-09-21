#!/usr/bin/env python
import sys

for line in sys.stdin:
    try:
        l = line.strip().split(',')
        if "endor" in l[0]:
            continue
        Pickup_longitude = l[5]
        Pickup_latitude = l[6]
        Tip_amount = l[14]
        Fare_amount = l[11]
        Pickup_longitude = float(Pickup_longitude)
        Pickup_latitude = float(Pickup_latitude)
        Tip_amount = float(Tip_amount)
        Fare_amount = float(Fare_amount)
        if Pickup_longitude==0 or Pickup_latitude==0:
            continue
        month = l[1][5:7]
        revenue = Tip_amount+Fare_amount
        Pickup_longitude = round(Pickup_longitude,4)
        Pickup_latitude = round(Pickup_latitude,4)
        print "%s,%s,%s\t%f" %(Pickup_longitude,Pickup_latitude,month,revenue)
    except:
        continue
