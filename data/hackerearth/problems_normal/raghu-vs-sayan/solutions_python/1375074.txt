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
	a,b,n=mapper(mi, ri().split())
	arr=mapper(mi, ri().split())
	arr.sort()
	r=s=0
	rout=sout=False
	for i in arr:
		if a-i>=0:
			a=a-i
			r+=1
		else:
			rout=True
		if b-i>=0:
			b=b-i
			s+=1
		else:
			sout=True
		if rout and sout:
			break
	if r>s:
		print "Raghu Won"
	elif s>r:
		print "Sayan Won"
	else:
		print "Tie"