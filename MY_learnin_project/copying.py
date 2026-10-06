import numpy as np

x = np.array([1, 2, 3])
y = x.copy()
y[0] = 23
print(x,y)