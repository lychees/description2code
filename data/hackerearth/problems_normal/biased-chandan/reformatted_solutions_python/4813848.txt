a = []
for i in xrange(input()):
    k = int(raw_input())
    if k:
        a.append(k)
    else:
        if len(a) > 0:
            a.pop()
print sum(a)
