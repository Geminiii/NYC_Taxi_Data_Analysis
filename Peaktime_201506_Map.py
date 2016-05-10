#!/usr/bin/env python
import sys
import os
from datetime import date

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
            daytag = "weekend"
            if date(int(year),int(month),int(day)).weekday()<=4:
                daytag = "weekday"
            if int(minute) < 30:
                print "green,%s,%s,%s\t%d" %(daytag,hour,"0",1)
            else:
                print "green,%s,%s,%s\t%d" %(daytag,hour,"30",1)
        if "yellow" in name:
            if l[0] == "VendorID":
                continue
            ymd,time = l[1].split(' ')
            year,month,day = ymd.split('-')
            hour,minute,second = time.split(':')
            daytag = "weekend"
            if date(int(year),int(month),int(day)).weekday()<=4:
                daytag = "weekday"
            if int(minute) < 30:
                print "yellow,%s,%s,%s\t%d" %(daytag,hour,"0",1)
            else:
                print "yellow,%s,%s,%s\t%d" %(daytag,hour,"30",1)
        if "citibike" in name:
            if l[0] == "tripduration":
                continue
            ymd,time = l[1].split(' ')
            month,day,year = ymd.split('/')
            hour,minute = time.split(':')
            daytag = "weekend"
            if date(int(year),int(month),int(day)).weekday()<=4:
                daytag = "weekday"
            if int(minute) < 30:
                print "citibike,%s,%s,%s\t%d" %(daytag,hour,"0",1)
            else:
                print "citibike,%s,%s,%s\t%d" %(daytag,hour,"30",1)
        if "uber" in name:
            if l[0] == "Dispatching_base_num":
                continue
            ymd,time = l[1].split(' ')
            month,day,year = ymd.split('/')
            hour,minute = time.split(':')
            daytag = "weekend"
            if date(int(year),int(month),int(day)).weekday()<=4:
                daytag = "weekday"
            if int(minute) < 30:
                print "uber,%s,%s,%s\t%d" %(daytag,hour,"0",1)
            else:
                print "uber,%s,%s,%s\t%d" %(daytag,hour,"30",1)
    except:
        continue
