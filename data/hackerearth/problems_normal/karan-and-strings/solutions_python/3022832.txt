
t=input()
while t!=0:
	t-=1
	s=raw_input()
	a=[]
	for i in range(len(s)):
		try:
			if s[i]==s[i+1]:
				continue
			if s[i]!=s[i+1]:
				a.append(s[i])
		except:
			a.append(s[len(s)-1])
	print ''.join(a)