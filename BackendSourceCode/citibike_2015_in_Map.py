#!/usr/bin/env python
import sys

for line in sys.stdin:
    try:
        l = line.strip().split(',')
        if l[0] == "tripduration":
            continue
        end_station_id=l[7]
        end_station_name=l[8]
        end_station_latitude=round(float(l[9]),4)
        end_station_longitude=round(float(l[10]),4)
        print "%s\t%s,%s,%s" %(end_station_id,end_station_name,end_station_longitude,end_station_latitude)
    except:
        continue
