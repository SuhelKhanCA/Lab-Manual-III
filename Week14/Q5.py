import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
import warnings

warnings.filterwarnings("ignore")

# Load the dataset
df = pd.read_csv('temp.csv')

# a. Clean independent features (handling missing values and encoding nominal data)
# Check for missing values
print("Missing values:\n", df.isnull().sum())

# Fill missing values if necessary (example: fill with median for numerical features)
for col in df.columns[:-1]:  # Exclude the dependent feature 'y'
    if df[col].dtype in [np.float64, np.int64]:
        df[col].fillna(df[col].median(), inplace=True)

# Convert nominal feature 'x5' to dummy variables
df = pd.get_dummies(df, columns=['x5'], drop_first=True)

# Separate independent and dependent features
X = df.drop('y', axis=1)
y = df['y']

# b. Draw heatmap to show correlations among independent features
plt.figure(figsize=(10, 8))
correlation_matrix = X.corr()
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# c. Train dataset using Logistic Regression, Decision Tree, and Random Forest
# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Function to evaluate models
def evaluate_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    return accuracy, f1, y_pred

# Initialize models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier()
}

# Store results
results = {}
for model_name, model in models.items():
    accuracy, f1, y_pred = evaluate_model(model, X_train, X_test, y_train, y_test)
    results[model_name] = {"Accuracy": accuracy, "F1 Score": f1, "Predictions": y_pred}

# Print performance
print("\nModel Performance:")
for model_name, metrics in results.items():
    print(f"{model_name} - Accuracy: {metrics['Accuracy']:.4f}, F1 Score: {metrics['F1 Score']:.4f}")

# d. Draw confusion matrix of each model
for model_name, metrics in results.items():
    cm = confusion_matrix(y_test, metrics['Predictions'])
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap='Blues')
    plt.title(f'Confusion Matrix for {model_name}')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

# e. Check whether scaling improves performance or not
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split scaled dataset
X_train_scaled, X_test_scaled, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Evaluate models on scaled data
results_scaled = {}
for model_name, model in models.items():
    accuracy, f1, y_pred = evaluate_model(model, X_train_scaled, X_test_scaled, y_train, y_test)
    results_scaled[model_name] = {"Accuracy": accuracy, "F1 Score": f1, "Predictions": y_pred}

# Print scaled performance
print("\nModel Performance with Scaling:")
for model_name, metrics in results_scaled.items():
    print(f"{model_name} - Accuracy: {metrics['Accuracy']:.4f}, F1 Score: {metrics['F1 Score']:.4f}")

# Compare performances
print("\nPerformance Comparison:")
for model_name in results.keys():
    print(f"{model_name} - Original: Accuracy: {results[model_name]['Accuracy']:.4f}, F1: {results[model_name]['F1 Score']:.4f} | "
          f"Scaled: Accuracy: {results_scaled[model_name]['Accuracy']:.4f}, F1: {results_scaled[model_name]['F1 Score']:.4f}")
