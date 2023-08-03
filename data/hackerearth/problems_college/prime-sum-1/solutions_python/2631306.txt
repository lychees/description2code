t = int(raw_input())

prim = [1,2,3,5,7]

for i in range(t):
	n = int(raw_input())

	if n<1:
		print -1
		continue

	dp = []*n
	sumi = 0
	sumi+=n/7
	n%=7

	if n==1 or n==2 or n==3 or n==5:
		sumi+=1
	elif n:
		sumi+=2

	print sumi