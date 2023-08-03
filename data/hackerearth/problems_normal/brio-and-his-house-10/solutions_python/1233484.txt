import math
t=input()
while t>0:
	a,b,c=map(float, raw_input().split(" "))
	r=(a*b*c)/(math.sqrt((a+b+c)*(b+c-a)*(c+a-b)*(a+b-c)))
	print("%.4f" % (3.1415*r*r))
	t-=1