#!/usr/bin/env python
import sys
import json
import os
from shapely.geometry import shape, Point
from datetime import date

with open("reference") as f:
    js = json.load(f)

for line in sys.stdin:
    try:
        name = os.environ.get("mapreduce_map_input_file")
        l = line.strip().split(',')
        if "green" in name:
            if l[0] == "VendorID":
                continue
            ymd,time = l[1].split(' ')
            year,month,day = ymd.split('-')
            hour,minute,second = time.split(':')
            daytag = "weekday"
            if date(int(year),int(month),int(day)).weekday()>4:
                continue
            if int(hour) != 8 and int(hour) != 9:
                continue
            Pickup_longitude = float(l[5])
            Pickup_latitude = float(l[6])
            Dropoff_longitude = float(l[7])
            Dropoff_latitude = float(l[8])
            if Pickup_longitude==0 or Pickup_latitude==0 or Dropoff_longitude==0 or Dropoff_latitude==0:
                continue
            Pickup_longitude = round(Pickup_longitude,4)
            Pickup_latitude = round(Pickup_latitude,4)
            Dropoff_longitude = round(Dropoff_longitude,4)
            Dropoff_latitude = round(Dropoff_latitude,4)
            Pickup_point = Point(Pickup_longitude,Pickup_latitude)
            Dropoff_point = Point(Dropoff_longitude,Dropoff_latitude)
            Pickup_region = 0
            Dropoff_region = 0
            P_tag = 0
            D_tag = 0
            for feature in js['features']:
                if P_tag==1 and D_tag==1:
                    break
                Manhattan_region=feature['properties']['communityDistrict']
                if int(Manhattan_region)>=200:
                    continue
                polygon = shape(feature['geometry'])
                if P_tag==0:
                    if polygon.contains(Pickup_point):
                        Pickup_region=Manhattan_region
                        P_tag = 1
                if D_tag==0:
                    if polygon.contains(Dropoff_point):
                        Dropoff_region=Manhattan_region
                        D_tag = 1
            if P_tag==1 and D_tag==1:
                print "%d,%d\t%d" %(Pickup_region,Dropoff_region,1)

        if "yellow" in name:
            if l[0] == "VendorID":
                continue
            ymd,time = l[1].split(' ')
            year,month,day = ymd.split('-')
            hour,minute,second = time.split(':')
            daytag = "weekday"
            if date(int(year),int(month),int(day)).weekday()>4:
                continue
            if int(hour) != 8 and int(hour) != 9:
                continue
            Pickup_longitude = float(l[5])
            Pickup_latitude = float(l[6])
            Dropoff_longitude = float(l[9])
            Dropoff_latitude = float(l[10])
            if Pickup_longitude==0 or Pickup_latitude==0 or Dropoff_longitude==0 or Dropoff_latitude==0:
                continue
            Pickup_longitude = round(Pickup_longitude,4)
            Pickup_latitude = round(Pickup_latitude,4)
            Dropoff_longitude = round(Dropoff_longitude,4)
            Dropoff_latitude = round(Dropoff_latitude,4)
            Pickup_point = Point(Pickup_longitude,Pickup_latitude)
            Dropoff_point = Point(Dropoff_longitude,Dropoff_latitude)
            Pickup_region = 0
            Dropoff_region = 0
            P_tag = 0
            D_tag = 0
            for feature in js['features']:
                if P_tag==1 and D_tag==1:
                    break
                Manhattan_region=feature['properties']['communityDistrict']
                if int(Manhattan_region)>=200:
                    continue
                polygon = shape(feature['geometry'])
                if P_tag==0:
                    if polygon.contains(Pickup_point):
                        Pickup_region=Manhattan_region
                        P_tag = 1
                if D_tag==0:
                    if polygon.contains(Dropoff_point):
                        Dropoff_region=Manhattan_region
                        D_tag = 1
            if P_tag==1 and D_tag==1:
                print "%d,%d\t%d" %(Pickup_region,Dropoff_region,1)
                
    except:
        continue
            







            
