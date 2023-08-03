'''
# Read input from stdin and provide input before running code
 
name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
# print 'Hello World!'
n = int(raw_input())
i = 0
while i < n:
	try:
		tc = ""
		tc2 = ""
		ctr = 0
		tc = raw_input()
		tc2 = raw_input()
		
		if tc == "" or tc2 == "":
			print "0" 
			next
		
		j = 0
		while j < min(len(tc),len(tc2)):
			if tc[j] == tc2[j]:
				ctr = ctr + 1
			j = j + 1
		
		print ctr
		ctr = 0
		i = i + 1
	except (EOFError):
		print "0"
		break