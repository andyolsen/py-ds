import pandas as pd

# Load data.
data = pd.read_csv('CO2.csv')

# Print info about the data.
print('\nRaw data\n', data.head(26))
print('\nData types\n', data.dtypes)
print('\nData index\n', data.index)