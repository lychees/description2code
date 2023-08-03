from collections import *
from heapq import *
from bisect import *
from math import *
mapper=map
mi=int
mf=float
inf=mf('inf')
ri=raw_input


t=mi(ri())
while t>0:
	t-=1
	s=raw_input()
	total=[0,0,0,0]
	for i in s:
		if i=='r':
			total[0]+=1
		elif i=='u':
			total[1]+=1
		elif i=='b':
			total[2]+=1
		elif i=='y':
			total[3]+=1
	print min(total)