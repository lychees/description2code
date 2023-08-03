n=int(raw_input())
for i in range(n):
	sum=0
	x=raw_input()
	fp=x[:len(x)/2]
	if len(x)%2==0:
		sp=x[len(x)/2:]
	else:
		sp=x[len(x)/2+1:]
	for i in range(len(fp)):
		sum=sum+abs(ord(fp[i])-ord(sp[len(fp)-i-1]))
	print sum