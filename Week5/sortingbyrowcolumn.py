import numpy as np

# Create a sample 2D NumPy array
array = np.array([[5, 2, 9],
                  [1, 6, 4],
                  [3, 8, 7]])

print("Original Array:")
print(array)

# Case 1: Sort the array by the second row
# Get the indices that would sort the second row
sorted_indices_row = np.argsort(array[1])

# Use those indices to sort the entire array
sorted_array_row = array[:, sorted_indices_row]

print("\nSorted Array by the second row:")
print(sorted_array_row)

# Case 2: Sort the array by the second column
# Get the indices that would sort the second column
sorted_indices_col = np.argsort(array[:, 1])

# Use those indices to sort the entire array
sorted_array_col = array[sorted_indices_col]

print("\nSorted Array by the second column:")
print(sorted_array_col)
