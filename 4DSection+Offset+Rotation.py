import rhinoscriptsyntax as rs
import math as m

x1=rs.GetReal("please enter the origin of your section plane (x)")
y1=rs.GetReal("please enter the origin of your section plane (y)")
z1=rs.GetReal("please enter the origin of your section plane (z)")

const=rs.GetReal("please enter where you want to cut your 4-D surface(w-value)")

rotXW=rs.GetReal("Please enter rotation angle in XW plane")
rotYW=rs.GetReal("Please enter rotation angle in YW plane")

def Main():
    crvs=[]
    crvs1=[]
    ptsZ=[]
    ptsZ1=[]
    factor=12
    cXW=m.cos(rotXW*m.pi/180)
    cYW=m.cos(rotYW*m.pi/180)
    sXW=m.sin(rotXW*m.pi/180)
    sYW=m.sin(rotYW*m.pi/180)
    x=0
    y=0
    z=0
    w=const*cXW/2+const*cYW/2
    a=1
    b=.15
    res=12
    for i in range(factor):
        x=i*res-factor/2*res
        if len(ptsZ)>1:
            crvs.append(rs.AddCurve(ptsZ))
        ptsZ=[]
        if len(ptsZ1)>1:
            crvs1.append(rs.AddCurve(ptsZ1))
        ptsZ1=[]
        for j in range(factor):
            y=j*res-factor/2*res
            zsq=m.pow(x*cXW-const*sXW,pow)/a+m.pow(y*cYW-const*sYW,pow)/b-m.pow(w+x*sXW-y*sYW,pow)+m.pow((x-x1)*cXW-const*sXW,pow)+m.pow((y-y1)*cYW-const*sYW,pow)-m.pow(w+x*sXW-y*sYW,pow)
            if zsq>0:
                z=(m.pow(zsq,1/pow)+z1*2-m.pow(z1,1/pow))/2
                ptsZ.append(rs.PointAdd([x,y,z],[0,0,0]))
                ptsZ1.append(rs.PointAdd([x,y,-z],[0,0,0]))
            if zsq<0:
                z=-(m.pow(abs(zsq),1/pow)+z1*2-m.pow(z1,1/pow))/2
                ptsZ.append(rs.PointAdd([x,y,z],[0,0,0]))
                ptsZ1.append(rs.PointAdd([x,y,-z],[0,0,0]))
    srf1=rs.AddLoftSrf(crvs)
    srf2=rs.AddLoftSrf(crvs1)
    return [srf1[0],srf2[0],crvs[len(crvs)-1],crvs1[len(crvs1)-1],crvs[0],crvs1[0]]

result=Main()
srf1=result[0]
srf2=result[1]
lastCrvs=result[2:4]
firstCrvs=result[4:6]