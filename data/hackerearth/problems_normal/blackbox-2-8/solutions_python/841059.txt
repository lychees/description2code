from math import factorial as fact
t = input()
for  i in xrange(t):
	n = input()
	print sum(map(int,str(fact(n))))