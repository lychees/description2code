q = input()
while(q):
    q -= 1
    n,t = map(int,raw_input().split())
    while(t):
        t -= 1
        if(n%2):
            n -= (n+1)/2
        else:
            n -= n/2
        n -= n/4
    print n
