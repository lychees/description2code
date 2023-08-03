from bisect import bisect
mapper=map
mi=int
mf=float
inf=mf('inf')
ri=raw_input
n,m,q=mapper(mi, ri().split())
params=[]
for i in xrange(n):
	pa=mapper(mi, ri().split())
	params.append(pa)
for i in xrange(q):
	qu=mapper(mi, ri().split())
	level=[]
	for p in xrange(n):
		qp=qu[p]
		got=bisect(params[p],qp)
		level.append(got)
	print min(level)