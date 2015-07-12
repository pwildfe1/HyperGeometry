import rhinoscriptsyntax as rs
import math as m

def dotProduct(vec1,vec2):
    sum=0
    for i in range(len(vec1)):
        sum=sum+vec1[i]*vec2[i]
    return sum

def Main():
    vector1=[2,5,2,5]
    vector2=[5,6,5,6]
    print dotProduct(vector1,vector2)


Main()