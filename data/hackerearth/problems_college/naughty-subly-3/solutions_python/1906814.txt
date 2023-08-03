test=input()
arr=[]
c=0
arr=raw_input().split()
if len(arr)==test:
	print len(arr)-len(set(arr))