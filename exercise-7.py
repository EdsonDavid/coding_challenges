# Question: Convert a 1D array to a 2D array with 2 rows
# input: np.arange(10)
# output array([[0, 1, 2, 3, 4],
#               [5, 6, 7, 8, 9]])

import numpy as np

arr = np.arange(10).reshape(2,5)
print(arr)
