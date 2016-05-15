#!/usr/bin/env python

import glob
path = '/Users/Li/Documents/BigData/Project/NYC_Taxi_Data_Analysis/201506_weekend_1819_YG/*'
files = glob.glob(path)
l=[]
for file in files:
	with open(file) as f:
		for row in f:
			row=row.strip()
			tri=row.split(',')
			if(int(tri[0])<200 and int(tri[1])<200):
				t=[int(tri[0]),int(tri[1]),int(tri[2])]
				l.append(t)
l=sorted(l)
res=[]
resSub=[]
i=0
for subl in l:
	if i<13:
		resSub.append(subl[2])
		i+=1
	else:
		res.append(resSub)
		resSub=[]
		resSub.append(subl[2])
		i=1
print res