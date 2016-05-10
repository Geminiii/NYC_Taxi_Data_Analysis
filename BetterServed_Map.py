#!/usr/bin/env python
import sys

for line in sys.stdin:
    key,value = line.strip().split('\t')
    print "%s\t%s" %(key,value)
