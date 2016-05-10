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
        areaid = 0
        for feature in js['features']:
            polygon = shape(feature['geometry'])
            if polygon.contains(point):
                areaid=feature['id']
                break
        if areaid != 0:
            month,trips,revenue = value.split(',')
            print "%s,%s\t%s,%s" %(areaid,month,trips,revenue)
        else:
            continue
    except:
        continue
