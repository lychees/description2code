from sys import stdin
def roy_and_code_streak():
	data = (line for line in stdin.read().splitlines())
	t = int(next(data))
	for t in xrange(t):
		n = int(next(data))
		submissions = []
		result = []
		for i in xrange(n):
			s,r = map(int,next(data).split())
			submissions.append(s)
			result.append(r)
		ranges_to_check = []
		i = 0
		while i < n:
			while i < n and result[i] == 0:
				i += 1
			if i >= n:
				break
			start = i
			while i < n and result[i] == 1:
				i += 1
			ranges_to_check.append([start,i])
		used = [0]*1000010
		each_range_max = [0]
		for i in ranges_to_check:
			cnt = 0
			for j in xrange(i[0],i[1]):
				if used[submissions[j]] != 1:
					used[submissions[j]] = 1
					cnt += 1
			each_range_max.append(cnt)
		print max(each_range_max)
roy_and_code_streak()