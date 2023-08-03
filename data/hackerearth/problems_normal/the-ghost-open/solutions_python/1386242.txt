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
	t=mi(ri())
	while t>0:
		t-=1
		n=mi(ri())
		total=0
		while n>1:
			m=n/2
			total+=m
			m=n%2
			if m==1:
				n=n/2
				n+=1
			else:
				n=n/2
		print total