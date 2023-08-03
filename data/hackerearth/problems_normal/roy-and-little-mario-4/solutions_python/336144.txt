MOD = 1000000007
array = []
def calculate(n):
	array.append(0)
	array.append(1)
	array.append(2)
	array.append(4)
	for i in xrange(4,n+1):
		temp = (array[i-3]+array[i-2]+array[i-1])%MOD
		array.append(temp)
	print array[n]
	del array[:]
t = input()
T = t if 1<=t<=10 else exit(1)
for i in xrange(T):
	n = input()
	N = n if 1<=n<=100000 else exit(1)
	calculate(N)