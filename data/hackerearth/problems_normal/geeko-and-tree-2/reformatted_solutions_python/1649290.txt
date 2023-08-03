t = int(raw_input())
while t > 0:
    p = raw_input().split()
    # k- array tree
    k = int(p[0])
    # Number of levels
    h = int(p[1])
    # Number of nodes n = (k^h+1 - 1) / (k-1)
    n = (k ** (h+1) - 1) / (k - 1)
    t -= 1
    mod = 0
    while n > 0:
        mod += (n % 10)
        n = n / 10
    print mod
