# Even rows, odd columns

import numpy as np

arr = np.random.randint(1, 100, (5,6))

print(arr)

print("Even rows odd columns")
even_rows_odd_columns  = arr[0::2, 1::2]

print(even_rows_odd_columns)