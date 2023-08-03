n=input()
s=raw_input()
x=input()
s=s.split()
s=map(int,s)
f=0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if (s[i]+s[j]+s[k])==x:
                f=1
                break
if f==0:
    print 'False'
else:
    print 'True'
