a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
tc=input()
while tc>0:
	tc-=1
	s=raw_input()
	path=[]
	c=0
	for i in s:
		place=a.index(i)
		if c<place:
			r=place-c
			l=-1*(26-r)
		else:
			l=place-c
			r=26-abs(l)
		if abs(r)<=abs(l):
			path.append(r)
			c=place
		else:
			path.append(l)
			c=place
	for i in path:
		print i,
	print