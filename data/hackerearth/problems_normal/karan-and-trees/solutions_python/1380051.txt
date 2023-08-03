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
	l,r=mapper(mi, ri().split())
	lset=set([])
	rset=set([])
	a,b=l,r
	while l>=1:
		if l%2==0:
			l=l/2
		else:
			l=(l-1)/2
		lset.add(l)
	while r>=1:
		if r%2==0:
			r=r/2
		else:
			r=(r-1)/2
		rset.add(r)
	if a in lset or a in rset:
		print a
	elif b in lset or b in rset:
		print b
	else:
		print max(lset.intersection(rset))