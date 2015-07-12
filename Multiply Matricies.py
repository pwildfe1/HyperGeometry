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

def multiplyMatrix(matrixA,matrixB):
    result=[]
    test= False
    newEntry=[]
    #check if the dimensions are correct#
    if len(matrixA)==len(matrixB[0]):
        test=True
    
    #Automatically transposes the matrix if the dimensions don't fit
    elif len(matrixA)==len(matrixB) and len(matrixA)!=len(matrixB[0]):
        matrixB=transpose(matrixB)
        test=True
    
    #if transposition doesn't work either than the function stops
    elif len(matrixA) != len(matrixB[0]) and len(matrixA) != len(matrixB):
        return "bad dimensions"
    
    if test==True:
        for i in range(len(matrixA[0])):
            for j in range(len(matrixB)):
                sum=0
                for k in range(len(matrixA)):
                    sum=sum+matrixA[k][i]*matrixB[j][k]
                newEntry.append(sum)
        for z in range(len(matrixA[0])):
            n=len(matrixA[0])*z
            result.append(newEntry[n:n+len(matrixA[0])])
    return result

def Main():
    hello=[]
    testMatrix=[[10,5,5],[5,5,10]]
    testMatrix2=[[5,5],[10,10],[5,5]]
    vector1=[2,5,2,5]
    vector2=[5,6,5,6]
    print multiplyMatrix(testMatrix,testMatrix2)


Main()