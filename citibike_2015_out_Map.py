#!/usr/bin/env python
import sys

for line in sys.stdin:
    try:
        l = line.strip().split(',')
        if l[0] == "tripduration":
            continue
        start_station_id=l[3]
        start_station_name=l[4]
        start_station_latitude=round(float(l[5]),4)
        start_station_longitude=round(float(l[6]),4)
        print "%s\t%s,%s,%s" %(start_station_id,start_station_name,start_station_longitude,start_station_latitude)
    except:
        continue
