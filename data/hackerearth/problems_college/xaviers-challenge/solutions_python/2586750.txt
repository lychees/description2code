t=input()
for i in range(0,t):
    s=raw_input()
    w=0
    for j in range(0,len(s)):
        w+=ord(s[j])
    f= int(w/len(s))
    if f%2==0:
        print s
    else:
        print s[::-1]
