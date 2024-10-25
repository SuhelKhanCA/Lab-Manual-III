import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Generate random values for x1 and x2
np.random.seed(42)  # For reproducibility
x1 = np.random.rand(1000)  # Random values between 0 and 1
x2 = np.random.rand(1000)  # Random values between 0 and 1

# Generate random values for c
c = np.random.rand(1000)  # Random values between 0 and 1

# Calculate y based on the function y = x1^12 + 3*x2^2 + c
y = x1**12 + 3*x2**2 + c

# Combine x1 and x2 into a feature matrix
X = np.column_stack((x1, x2))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a PolynomialFeatures object
poly = PolynomialFeatures(degree=12)  # Set degree to 12
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)

# Train the Polynomial Regression model
model = LinearRegression()
model.fit(X_poly_train, y_train)

# Make predictions
y_pred = model.predict(X_poly_test)

# Calculate the R^2 score
score = r2_score(y_test, y_pred)
print(f"R^2 Score: {score}")
