t=input()
for i in range(t):
	x,y,z=[int(i) for i in raw_input().split()]
	if(x*y==z):
		print "YES"
	else:
		print "NO"