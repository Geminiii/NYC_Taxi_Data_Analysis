#!/usr/bin/env python
import sys
import json
from shapely.geometry import shape, Point

with open("reference") as f:
    js = json.load(f)

for line in sys.stdin:
    try:
        l = line.strip().split(',')
        if l[0] == "VendorID":
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
        point = Point(Pickup_longitude,Pickup_latitude)
        zipcode = ""
        for feature in js['features']:
            polygon = shape(feature['geometry'])
            if polygon.contains(point):
                zipcode=feature['properties']['postalCode']
                break
        if zipcode!="":
            print "%s,%s\t%f" %(zipcode,month,revenue)
        else:
            continue
    except:
        continue
