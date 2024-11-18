import numpy as np
import pandas as pd

# Read a CSV file, get a Pandas DataFrame back, and assign the 'Precipitation' column to a NumPy array.
dataframe = pd.read_csv('BergenWeather2019.csv')
precipitation = np.array(dataframe['Precipitation'])
precipitation = np.around(precipitation / (10 * 2.54), 4)
print('\nPrecipitation inches to 4dp\n', precipitation)

# Use Boolean operations on a NumPy array.
print('\nPrecipitation on this day?:\n', precipitation > 0)
print('\n1 to 2 inces of precipitation on this day?:\n', (precipitation >= 1) & (precipitation <= 2))

# Use Boolean aggregation on a NumPy array.
print('Were there any days with more than 2 inches of precipitation?', np.any(precipitation > 2))
print('How many days had more than 2 inches of precipitation?:      ', np.count_nonzero(precipitation > 2))