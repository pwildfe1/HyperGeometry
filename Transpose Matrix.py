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

def Main():
    hello=[]
    testMatrix=[[10,15,20],[10,15,15],[10,15,14]]
    print transpose(testMatrix)


Main()