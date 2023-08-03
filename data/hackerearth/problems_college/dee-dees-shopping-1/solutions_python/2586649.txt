t=input()
for i in range(0,t):
    n=input()
    f=0
    list=[]
    for i in range(0,19):
        for j in range(0,14):
            if 6*i+8*j==n:
                f=1
                list.append(i+j)
    if f==1:
        print min(list)
    else:
        print -1
