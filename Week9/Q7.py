import pandas as pd

df = pd.read_csv('employee_data.csv')
df.head()
df['HRA'] = df['salary'] * 0.18

df.head()