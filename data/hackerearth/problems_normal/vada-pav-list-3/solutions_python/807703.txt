names = []
n = input()
for i in xrange(n):
	r = raw_input()
	names.append(r)
finallist = sorted(set(names))
print len(finallist)
for i in finallist:
	print i