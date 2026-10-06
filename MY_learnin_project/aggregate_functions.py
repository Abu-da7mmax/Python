import numpy as np

array = np.array([[1, 5, 3, 4],
                  [5, 6, 7, 8]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array)) #standard deviation
print(np.min(array))
print(np.max(array))
print(np.var(array)) #variance
print(np.sum(array, axis = 0)) # to calculate all colums
print(np.sum(array, axis = 1)) # to calculate all rows