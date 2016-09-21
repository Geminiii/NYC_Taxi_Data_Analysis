#!/usr/bin/env python
import sys

for line in sys.stdin:
    try:
        key,value = line.strip().split('\t')
        month,trips,revenue = value.split(',')
        print "%s\t%s,%s" %(key,month,trips)
    except:
        continue
