import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# 1. Generate continuous independent features (x1, x2, x3, x4)
n_samples = 1000  # Number of samples

x1 = np.random.normal(loc=50, scale=10, size=n_samples)  # Normal distribution: mean=50, std=10
x2 = np.random.normal(loc=30, scale=5, size=n_samples)   # Normal distribution: mean=30, std=5
x3 = np.random.normal(loc=100, scale=15, size=n_samples) # Normal distribution: mean=100, std=15
x4 = np.random.normal(loc=5, scale=1, size=n_samples)    # Normal distribution: mean=5, std=1

# 2. Generate the nominal feature (x5)
categories = ['A', 'B', 'C']  # Possible categories for x5
x5 = np.random.choice(categories, size=n_samples)

# 3. Generate the dependent feature (y)
# We will simulate a binary classification with some dependency on the independent variables
# For simplicity, let's assume a random binary outcome (0 or 1) based on some noise.
y = np.random.choice([0, 1], size=n_samples)

# 4. Create a DataFrame
df = pd.DataFrame({
    'x1': x1,
    'x2': x2,
    'x3': x3,
    'x4': x4,
    'x5': x5,
    'y': y
})

# Check the first few rows of the generated data
print(df.head())

# Save the DataFrame to a CSV file if needed
df.to_csv('temp.csv', index=False)
