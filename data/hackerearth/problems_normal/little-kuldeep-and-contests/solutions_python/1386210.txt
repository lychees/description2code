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

	times=[]
	flag=False
	for i in xrange(n):
		t=ri().split("-")
		s=t[0].split(':')
		e=t[1].split(':')
		st=int(s[0]+s[1])
		et=int(e[0]+e[1])
		for j in times:
			if (j[0]<st and j[1]>st) or (j[0]<et and et<j[1]) or (j[0]>st and j[1]<et):
				print "Will need a moderator!"
				flag=True
				break
		times.append((st,et))
		if flag:
			break
	if not flag:
		print "Who needs a moderator?"
		