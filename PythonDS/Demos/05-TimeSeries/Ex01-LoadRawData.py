import pandas as pd

# Load data.
data = pd.read_csv('Sales.csv')

print('\nRaw data\n', data.head())
print('\nData types\n', data.dtypes)
print('\nData index\n', data.index)