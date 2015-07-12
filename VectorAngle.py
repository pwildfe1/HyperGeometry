import rhinoscriptsyntax as rs
import math as m

def dotProduct(vec1,vec2):
    sum=0
    for i in range(len(vec1)):
        sum=sum+vec1[i]*vec2[i]
    return sum

def lenVec(vec):
    sum=0
    for i in range(len(vec)):
        sum+=m.pow(vec[i],2)
    return m.pow(sum,.5)

def vectAngle(vec1,vec2):
    ang=m.acos(dotProduct(vec1,vec2)/(lenVec(vec1)*lenVec(vec2)))
    return ang

def Main():
    vector1=[1,0,0,0]
    vector2=[0,0,0,1]
    print vectAngle(vector1,vector2)


Main()