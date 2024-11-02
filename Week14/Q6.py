import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Set the random seed for reproducibility
np.random.seed(42)

# Generate 1000 random values for x between 0 and 1
x = np.random.rand(1000)

# Generate 1000 random values for k (for example, uniformly between -1 and 1)
k = np.random.uniform(-1, 1, size=1000)

# Calculate y based on the function y = 3x + k
y = 3 * x + k

# Reshape x for sklearn
x = x.reshape(-1, 1)

# Create a DataFrame (optional, for clarity)
data = pd.DataFrame({'x': x.flatten(), 'y': y})

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data[['x']], data['y'], test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
score = r2_score(y_test, y_pred)

# Print the model's R^2 score
print(f"R^2 Score of the Linear Regression model: {score:.4f}")
