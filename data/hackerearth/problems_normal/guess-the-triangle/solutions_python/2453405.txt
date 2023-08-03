x=[]
y=[]
xs=0
ys=0
for i in range(0,3):
    s=raw_input()
    s=s.split()
    xs=xs+float(s[0])
    x.append(2*float(s[0]))
    ys=ys+float(s[1])
    y.append(2*float(s[1]))
xc=[]
yc=[]
for i in range(0,3):
    xc.append(xs-x[i])
    yc.append(ys-y[i])
for i in range(0,3):
    for j in range(0,3-i-1):
        if xc[j]>xc[j+1]:
            xc[j],xc[j+1]=xc[j+1],xc[j]
            yc[j],yc[j+1]=yc[j+1],yc[j]
        if(xc[j]==xc[j+1]):
            if yc[j]>yc[j+1]:
                xc[j],xc[j+1]=xc[j+1],xc[j]
                yc[j],yc[j+1]=yc[j+1],yc[j]
for i in range(0,3):
    print("%.4f" % xc[i]),
    print("%.4f" % yc[i])
