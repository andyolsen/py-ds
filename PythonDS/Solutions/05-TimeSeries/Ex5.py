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

# Resample the data - combine all the readings for a month into a single (mean) value.
ts = ts.resample('MS').mean()
print('\nResampled data, single (mean) value per month\n', ts.head(12))

# Index into data in various ways.
print('\nCO2 reading for July 1958\n', ts['1958-07'])
print('\nCO2 readings for July-December 1958\n', ts['1958-07' : '1958-12'])
print('\nCO2 readings for all months up to December 1958\n', ts[ : '1958-12'])
print('\nCO2 readings for all months from July 1997 onwards\n', ts['1997-07' :])
print('\nCO2 readings for all months in 1997\n', ts['1997'])

# Get some info about these values, e.g. for CO2 in 1997.
print('\nCO2 1997 info\n', ts['1997'].describe())