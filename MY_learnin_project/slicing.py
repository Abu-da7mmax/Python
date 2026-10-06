import numpy as np

array = np.array([[1, 2, 3, 4],
                  [2, 3,4, 6],
                  [6, 7, 8, 9],
                  [10,11,13,24]])

print(array[1:4]) # start:end:step
print(array[3, 3])
print(array[:,2])
print(array.ndim)
print(array.shape)
print(array.size)
print(array.dtype)