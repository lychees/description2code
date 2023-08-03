from collections import *
from heapq import *
from bisect import *
from math import *
from itertools import *
inf=float('inf')
from fractions import gcd

if __name__=="__main__":
	tcase=int(raw_input())
	while tcase>0:
		tcase-=1
		a,b,c=map(int,raw_input().split())
		mgcd=gcd(a, gcd(b,c))
		ans=((a/mgcd)*(b/mgcd))%1000000007
		print mgcd,(ans*c/mgcd)%1000000007