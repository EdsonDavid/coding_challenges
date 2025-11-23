# Question : Create a 3×3 numpy array of all True’s

# Solution
import numpy as np

x = np.full((3,3), True, dtype=bool)
print(x)

#OR

x = np.full(9,True,dtype=bool).reshape((3,3))
print(x)

#OR

x = np.ones((3,3),dtype=bool)
print(x)