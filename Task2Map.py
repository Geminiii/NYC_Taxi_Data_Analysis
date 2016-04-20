#!/usr/bin/env python
import sys
import os

for line in sys.stdin:
    try:
        name = os.environ.get("mapreduce_map_input_file")
        l = line.strip().split(',')
        if "green" in name:
            if l[0] == "VendorID":
                continue
            hour = l[1][11:13]
            print "green,%s\t%d" %(hour,1)
        if "yellow" in name:
            if l[0] == "VendorID":
                continue
            hour = l[1][11:13]
            print "yellow,%s\t%d" %(hour,1)
        if "citibike" in name:
            if l[0] == "tripduration":
                continue
            hour = ((l[1].split(' ')[1]).split(':'))[0]
            print "citibike,%s\t%d" %(hour,1)
    except:
        continue
