t = input()
powers = list(map(int,raw_input().split()))
zombies = filter(lambda x: (x%2==0),powers)
vampires = filter(lambda x: (x%2==1),powers)
zombies.sort()
zombie_pow = sum(zombies)
vampires.sort()
vampire_pow = sum(vampires)
powers = zombies+[zombie_pow]+vampires+[vampire_pow]
for a in powers:
    print a,
