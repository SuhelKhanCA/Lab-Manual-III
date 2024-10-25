import pandas as pd

employees = pd.read_csv('employees.csv', names=['Name', 'EId', 'Salary', 'DID'])
departments = pd.read_csv('departments.csv', names=['DID', 'DName', 'DLocation'])

df = pd.merge(employees, departments, on='DID')

df.to_csv('merged_data.csv', index=False)

print("Merged data saved to 'merged_data.csv'.")
