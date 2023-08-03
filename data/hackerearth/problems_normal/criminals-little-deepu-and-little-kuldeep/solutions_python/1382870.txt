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
	n=l=mi(ri())
	arr=[]
	total=0
	while n>0:
		n-=1
		arr.append(mi(ri()))
	arr.sort()
	total=0
	tmparr=[]
	improve=True
	while improve:
		p=arr[0]
		got=False
		for i in xrange(1,len(arr)):
			if arr[i]>p:
				got=True
				p=arr[i]
			else:
				tmparr.append(arr[i])
		if got:
			total+=1
			if len(tmparr)>0:
				arr=[]
				arr=tmparr
				arr.sort()
				tmparr=[]
			else:
				break
		else:
			total+=1
			if len(tmparr)>0:
				arr=[]
				arr=tmparr
				arr.sort()
				tmparr=[]
			else:
				break
	print total