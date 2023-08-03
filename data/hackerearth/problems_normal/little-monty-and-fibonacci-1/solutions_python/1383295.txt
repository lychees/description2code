from collections import *
from heapq import *
from bisect import *
from math import *
mapper=map
mi=int
mf=float
inf=mf('inf')
ri=raw_input

d={}
fibs=[1,1]
ns=[]
t=mi(ri())
while t>0:
	t-=1
	ns.append(mi(ri()))
a=b=1
while len(fibs)<1000:
	a,b=b,a+b
	fibs.append(b)

dp=[0]*1000
dp[0]=1
dp[1]=4
for i in xrange(2,1000):
	total=dp[i-1]
	now=fibs[i]
	for j in fibs[:i+1]:
		if now%j==0:
			total+=1
	dp[i]=total
for i in ns:
	print dp[i-1]