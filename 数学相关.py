import numpy as np

A = np.array([[1, -1, -1],
             [2, -1, -3],
             [-3, 4, 4]])
B = np.array([[1, 2, 3],
             [2, 2, 1],
             [3, 4, 3]])
print(B.transpose().dot(A))
print(np.linalg.inv(A))
print(A.dot(np.linalg.inv(A)))

