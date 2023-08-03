t = input()
for k in range(0,t):
	n = input()
	s = raw_input()
	s = s.split()
	s = map(int,s)
	st = -1
	l = -1
	for i in range(0,len(s)-1):
		if(s[i] > s[i+1]):
			st = i
			break
	if(st != -1):
		for i in range(st,len(s)-1):
			if(s[i] < s[i+1]):
				l = i
				break
		if(l == -1):
			l = len(s)-1
		temp = s[st:l+1]
		temp = temp[::-1]
		ans = s[0:st]
		for i in range(0,len(temp)):
			ans.append(temp[i])
		for i in range(l+1,len(s)):
			ans.append(s[i])
		flag = 0
		for i in range(0,len(ans)-1):
			if(ans[i] > ans[i+1]):
				flag = 1
				break		
		if(flag == 0):
			print st+1,l+1
		else:
			print -1,-1
	else:
		print -1,-1
