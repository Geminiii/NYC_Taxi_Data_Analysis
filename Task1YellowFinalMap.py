#!/usr/bin/env python
import sys
import json
from shapely.geometry import shape, Point

with open("reference") as f:
    js = json.load(f)

for line in sys.stdin:
    try:
        key,value = line.strip().split('\t')
        longitude,latitude = key.split(',')
        longitude = float(longitude)
        latitude = float(latitude)
        point = Point(longitude,latitude)
        zipcode = ""
        for feature in js['features']:
            polygon = shape(feature['geometry'])
            if polygon.contains(point):
                zipcode=feature['properties']['postalCode']
                break
        if zipcode!="":
            month,trips,revenue = value.split(',')
            print "%s,%s\t%s,%s" %(zipcode,month,trips,revenue)
        else:
            continue
    except:
        continue
