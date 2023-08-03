T=int(raw_input())
L=[]
while T>0:
    Branches,Levels=raw_input().split()
    Branches=int(Branches)
    Levels=int(Levels)
    Numerator=Branches**(Levels+1)-1
    Denominator=Branches-1
    Nodes=Numerator/Denominator
    Ans=0
    while Nodes>0:
        Ans=Ans+Nodes%10
        Nodes=Nodes/10
    L.append(Ans)
    T=T-1


for x in L:
    print(x)