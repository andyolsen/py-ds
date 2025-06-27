import pandas as pd

# Load data.
data = pd.read_csv('CO2.csv', 
                   parse_dates=['date'], 
				   index_col='date')

# Get the co2 column as a Pandas Series object.
ts = data['co2']

# Print info about the data.
print('\nParsed data\n', ts.head(26))
print('\nData types\n', ts.dtypes)
print('\nData index\n', ts.index)