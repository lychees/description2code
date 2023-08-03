a,b,n= map(int,raw_input().split())
fib=[]
fib.append(a)
fib.append(b)
for i in range(2,15):
		fib.append(fib[i-1]+fib[i-2])
print fib[n-1]
