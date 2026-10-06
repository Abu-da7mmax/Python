import numpy as np

sc = np.array([1, 5, 3, 4])
cs = np.array([5, 6, 7, 8])

#All the benifits of numpy arithmetics
print(sc + 1)
print(sc ** 5)
print(np.sqrt(sc))
print(np.round(sc)) #there two other types for rounding, if you wanna round up use "ceil" if you wanna round down use "floor"
print(np.pi * sc ** 2)
print(sc + cs)
print(sc == 1) #If matched will give a boolen output "True" or "False"
