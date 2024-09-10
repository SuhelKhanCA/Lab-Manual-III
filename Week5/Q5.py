import numpy as np

def create_and_extract_array():
    # Create a random 5x5 NumPy array (you can adjust the size as needed)
    rows, cols = 5, 5
    random_array = np.random.randint(1, 100, size=(rows, cols))

    # Extract odd rows and even columns
    odd_rows = random_array[::2]  # Select every 2nd row (odd rows)
    even_columns = random_array[:, 1::2]  # Select every 2nd column (even columns)

    return odd_rows, even_columns

# Example usage
odd_rows_result, even_columns_result = create_and_extract_array()

print("Odd rows:")
print(odd_rows_result)

print("\nEven columns:")
print(even_columns_result)
