from collections import *
from heapq import *
from bisect import *
from math import *
from itertools import *
mapper=map
mi=int
mf=float
inf=mf('inf')
ri=raw_input

if __name__=="__main__":
	n=mi(ri())
	cities=[]
	for i in xrange(n):
		cities.append(ri())
	costs=[]
	for i in xrange(n):
		row=mapper(mi, ri().split())
		costs.append(row)
	pathlen=mi(ri())
	totalcost=0
	present=0
	for i in xrange(pathlen):
		to=ri()
		ind=cities.index(to)
		totalcost+=costs[present][ind]
		present=ind
	print totalcost

	