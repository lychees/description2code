t=input()
for k in range(0,t):
    s=raw_input()
    r=raw_input()
    c=0
    for i in range(0,len(s)):
        a=''
        for j in range(0,i):
            a=a+s[j]
        a=a+r
        for j in range(i,len(s)):
            a=a+s[j]
        b=a[::-1]
        if b==a:
            c=c+1
    a=s+r
    b=a[::-1]
    if a==b:
        c=c+1
    print c
