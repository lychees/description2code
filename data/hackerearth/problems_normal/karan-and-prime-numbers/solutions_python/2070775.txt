def primes(n): # sieve of eratosthenes
    ps, sieve = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
           ps.append(p)
           for i in range(p * p, n + 1, p):
               sieve[i] = False
    return ps
    
t = input()
while(t):
    t -= 1
    start,end = map(int,raw_input().split())
    arr = primes(end)
    arr = filter(lambda x: x>=start,arr)
    print sum(arr)