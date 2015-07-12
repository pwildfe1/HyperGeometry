import rhinoscriptsyntax as rs
import math as m

def centerPoint(object):
    if rs.IsMesh(object):
        centers=rs.MeshFaceCenters(object)
        for i in range(len(centers)):
            if i==0:
                sumPoint=centers[0]
            else:
                sumPoint=rs.PointAdd(sumPoint,centers[i])
        cpt=sumPoint/len(centers)
    if rs.IsCurve(object):
        pts=rs.DivideCurve(object,100)
        for i in range(len(pts)):
            if i==0:
                sumPoint=pts[0]
            else:
                sumPoint=rs.PointAdd(sumPoint,pts[i])
        cpt=sumPoint/len(pts)
    return cpt