import numpy as np

random = np.random.default_rng(seed = 1) # you can same the same numbers in the matrix if u put "seed = 1" inside the brackets ()

print(random.integers(1,8)) #Last number is exclusive
print(random.integers(1, 8, size = 4)) #gives 4 random numbers in one dimension 1*4
print("-----------------S")
print(random.integers(1, 8, size = (4, 4)),"\n") # random 4*4 matrix 

#random float numbers
print("Random float numbers")
np.random.seed(seed = 1) 
float = np.random.uniform(-1, 1, size = (3, 3))
print(float)

#random shuffling and choice
print("---------------------------\nrandom shuffling and choices\n")
rng = np.random.default_rng()
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)
choice = rng.choice(array)
print(choice)

#there is a function that will be important in ML which is "np.random.rand(put any number of indecies)"