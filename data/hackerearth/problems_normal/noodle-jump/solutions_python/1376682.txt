from collections import *
from heapq import *
from bisect import *
from math import *
mapper=map
mi=int
mf=float
inf=mf('inf')
ri=raw_input


n,mj=mapper(mi, ri().split())
arr=mapper(mi, ri().split())
arr.sort()
if arr[0]<=mj:
	pos=arr[0]
	for i in xrange(1,n):
		dis=arr[i]-arr[i-1]
		if dis<=mj:
			pos=arr[i]
		else:
			break
else:
	pos=0
print pos