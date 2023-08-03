n = input()
s = map(int,raw_input().split())
sum_s = [0 for i in range(0,3)]
for i in range(0,len(s)):
	sum_s[i%3] += s[i]
print sum_s[0],sum_s[1],sum_s[2] 