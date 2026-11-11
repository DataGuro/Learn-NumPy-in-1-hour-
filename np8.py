import numpy as np

"""
Brosdcasting allows NumPy to perform operations on arrays
with diffrent shapes by virtually exapanding dimensions
so they matsch the larger array's shape.


The dimensions have the same size.
OR
One of the dimensions has a size of 1.
"""

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)
print(array2.shape)

print("=" * 60)

print(array1 * array2)

print("=" * 60)

array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(array1.shape)
print(array2.shape)

print("=" * 60)

print(array1 * array2)