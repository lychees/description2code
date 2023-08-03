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
	s=ri()
	slen=len(s)
	total=0
	before=0
	thr=False
	ass=0
	for i in xrange(slen):
		place=i
		if s[i]=='a' or s[i]=='z':
			ass+=1
			thr=True
			left=before
			right=slen-i-1
			tmp=left+right+(left*right)
			if (left+right)==slen-1:
				tmp-=1
			total+=tmp
			before=0
		else:
			before+=1
	if thr:
		total+=ass+1

	print total