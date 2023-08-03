def reverse(s):
    le=len(s)
    l=le/2
    s=s[::-1]
    return s

t=int(raw_input())
ii=0
while t>0:
    ii+=1
    #print ii
    t-=1
    a, b=raw_input().split()
    a=reverse(a)
    #print a
    b=reverse(b)
    #print b
    a=int(a)+int(b)
    a=str(a)
    a=reverse(a)
    a=int(a)
    a=str(a)
    print a
