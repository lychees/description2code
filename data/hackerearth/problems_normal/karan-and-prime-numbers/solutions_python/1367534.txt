import math
import random
t=int(raw_input())

def isprime(n):
	if n==2:
		return True
	if n&1==0 or n==1:
		return False
	for i in xrange(2,int(math.sqrt(n))+1):
		if n%i==0:
			return False
	return True
while t>0:
	t-=1
	a,b=map(int, raw_input().split())
	total=0
	for x in xrange(a,b+1):
		if isprime(x):
			total+=x
	print total