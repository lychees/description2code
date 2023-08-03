sol = 0
tc = input()
rq = set(map(int,raw_input().split()))
m = input()
for _ in xrange(m):
	gq = list(map(int,raw_input().split()))
	if(set.intersection(rq,gq) == rq):
		sol+=1
print sol