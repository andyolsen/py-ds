import pandas as pd

import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

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

# Let's just look at the last 1990 - 2000, group data by year, and plot the years side-by-side for comparison.
tsSlice = ts['1990' : '2000']

groups = tsSlice.groupby(pd.Grouper(level='date', freq='Y'))
annualizedData = pd.DataFrame()
for dateIndex, group in groups:
    annualizedData[dateIndex.year] = group.values
print('\nAnnualized data\n', annualizedData)

# Plot as subplots.
annualizedData.plot(subplots=True, legend=True)
plt.show()

# Plot as boxplots with whiskers.
annualizedData.boxplot()
plt.show()