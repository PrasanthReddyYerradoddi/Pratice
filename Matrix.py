import numpy as np

M = np.array([[1,2,3],[4,5,6],[7,8,9]])
N = np.array([[9,8,7],[6,5,4],[3,2,1]])

i = 0
j = 0
print(M[i-1][j])
print(M[i+1][j])
print(M[i][j-1])
print(M[i][j+1])

