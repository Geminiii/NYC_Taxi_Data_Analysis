#!/usr/bin/env python
import sys
import json
from shapely.geometry import shape, Point

with open("reference") as f:
    js = json.load(f)

for line in sys.stdin:
    try:
        longitude,latitude,car,trips = line.strip().split(',')
        longitude = float(longitude)
        latitude = float(latitude)
        point = Point(longitude,latitude)
        Pickup_region = 0
        for feature in js['features']:
            polygon = shape(feature['geometry'])
            if polygon.contains(point):
                Pickup_region=feature['id']
                break
        print "%d\t%s,%s" %(Pickup_region,car,trips)
    except:
        continue
