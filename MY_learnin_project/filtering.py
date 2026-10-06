import numpy as np

ages = np.array([[17,12,33,44,19,29,11], 
                 [13,22,24,35,75,27,23]])
teenagers = ages[ages < 24]
adults = ages[ (ages >= 18) & (ages < 50)]
even_ages = ages[ages % 2 == 0]
odd_ages = ages[ages % 2 != 0]
preserving_the_shape = np.where(ages >= 18, ages, 0)
print(teenagers)
print(adults)
print(even_ages)
print(odd_ages)
print("--------------------------------------------")
print(preserving_the_shape) #for the matrix to fully showing the places of ages and replacing the non matching conditions with "0"