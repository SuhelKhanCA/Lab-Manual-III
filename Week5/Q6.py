# Program to sort by row and column

import numpy as np

arr = np.random.randint(1, 100, (5, 6))

# case 1

arr[1, :].sort()

print(arr)

# case 2

arr[:, 1].sort()

print(arr)

