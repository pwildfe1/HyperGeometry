import rhinoscriptsyntax as rs
import math as m

def transpose(matrix):
    newMatrix=[]
    newEntry=[]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            newEntry.append(matrix[j][i])
    for k in range(len(matrix[0])):
        n=len(matrix)*k
        newMatrix.append(newEntry[n:n+len(matrix)])
    return newMatrix

def transformVec(vec,transform):
    result=[]
    test= False
    newEntry=[]
    #check if the dimensions are correct#
    if len(vec)==len(transform[0]):
        test=True
    
    #Automatically transposes the matrix if the dimensions don't fit
    elif len(vec)==len(transform) and len(transform[0])!=1:
        matrixB=transpose(matrixB)
        test=True
    
    #if transposition doesn't work either than the function stops
    elif  len(transform[0])!=1 and len(vec)!=len(transform):
        return "bad dimensions"
    
    if test==True:
        for i in range(len(transform)):
            sum=0
            for j in range(len(vec)):
                sum=sum+vec[j]*transform[i][j]
            result.append(sum)
    return result

def Main():
    hello=[]
    testMatrix=[[10,5,5],[5,5,10]]
    testMatrix2=[[5,5],[10,10],[5,5]]
    vector1=[2,5,2]
    vector2=[5,6,5,6]
    print transformVec(vector1,testMatrix)


Main()