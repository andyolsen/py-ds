import pandas as pd

# Load data.
data = pd.read_csv('CO2.csv', 
                   parse_dates=['date'], 
				   index_col='date')

# Get the co2 column as a Pandas Series object.
ts = data['co2']
print('\nParsed data\n', ts.head(26))

# Fill in each hole with the next available value.
ts = ts.fillna(method='bfill')
print('\nParsed data, filled-in holes\n', ts.head(26))