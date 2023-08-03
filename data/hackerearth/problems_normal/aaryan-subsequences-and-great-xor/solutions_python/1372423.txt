n=input()
arr=map(int,raw_input().split())
final=0
for i in xrange(0,n):
	final|=arr[i]
print final