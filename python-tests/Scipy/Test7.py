#Scipy subpackage for Linear algebra
#Inverse of matrix
import numpy as np
from scipy import linalg
matrix = np.array([[10,6],[2,7]])
matrix

type(matrix)

linalg.inv(matrix)

#Finding Determinant
linalg.det(matrix)

#Solving Linear equations
#2x+3y+z=21,-x+5y+4z=9,3x+2y+9z=6
numArray = np.array([[2,3,1],[-1,5,4],[3,2,9]])
numres = np.array([21,9,6])
numArray
numres
res = np.linalg.solve(numArray,numres)
res

np.allclose(np.dot(numArray,res),numres)
#single value decomposition
numSvdArr = np.array([[3,5,1],[9,5,7]])
numSvdArr.shape

linalg.svd(numSvdArr)
linalg.svd(numArray)

#Calculate eigenvalues and eigenvector
#creating a test dataset from a rating system on a scale of 1 to 10 as numpy array
test_rating_data = np.array([[5,8],[7,9]])

#using eig of linalg package
eigenValues, eigenVector = linalg.eig(test_rating_data)
first_eigen,second_eigen = eigenValues

print(first_eigen,second_eigen)

#apply slizing technique to get first and second eigenvector
print(eigenVector[:,0])
print(eigenVector[:,1])

