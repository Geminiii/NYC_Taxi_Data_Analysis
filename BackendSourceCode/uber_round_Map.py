#!/usr/bin/env python
import sys
import os

for line in sys.stdin:
    try:
        name = os.environ.get("mapreduce_map_input_file")
        l = line.strip().split(',')
        if "green" in name:
            if "endor" in l[0]:
                continue
            Pickup_longitude = round(float(l[5]),4)
            Pickup_latitude = round(float(l[6]),4)
            if Pickup_longitude==0 or Pickup_latitude==0:
                continue
            print "%f,%f,green\t%d" %(Pickup_longitude,Pickup_latitude,1)
        if "yellow" in name:
            if "endor" in l[0]:
                continue
            Pickup_longitude = round(float(l[5]),4)
            Pickup_latitude = round(float(l[6]),4)
            if Pickup_longitude==0 or Pickup_latitude==0:
                continue
            print "%f,%f,yellow\t%d" %(Pickup_longitude,Pickup_latitude,1)
        
        if "uber" in name:
            if l[0] == "Dispatching_base_num":
                continue
            Pickup_longitude = float(l[2])
            Pickup_latitude = float(l[1])
            if Pickup_longitude==0 or Pickup_latitude==0:
                continue
            print "%f,%f,uber\t%d" %(Pickup_longitude,Pickup_latitude,1)
    except:
        continue
