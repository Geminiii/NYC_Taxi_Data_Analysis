#!/usr/bin/env python
import sys

current_key = ""
current_green_810 = 0
current_all_810 = 0
current_all_57 = 0
regionlist=[]

for line in sys.stdin:
    key,value = line.strip().split('\t')
    car,trips_57,trips_810 = value.split(',')
    trips_57 = int(trips_57)
    trips_810 = int(trips_810)
    if current_key == key:
        if car == "green":
            current_green_810 += trips_810
            current_all_810 += trips_810
        else:
            current_all_810 += trips_810
            current_all_57 += trips_57
    else:
        if current_key != "":
            regionlist.append((current_key,current_green_810))
        current_key = key
        if car == "green":
            current_green_810 = trips_810
            current_all_810 += trips_810
        else:
            current_all_810 += trips_810
            current_all_57 += trips_57
if current_key != "":
    regionlist.append((current_key,current_green_810))
all_difference = current_all_810 - current_all_57
for region in regionlist:
    regionid = region[0]
    green_810 = region[1]
    result = float(green_810)/float(all_difference)
    print "%s,%f" %(regionid,result)

