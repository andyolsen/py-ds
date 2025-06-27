import numpy as np
import pandas as pd

# Read a CSV file, get a Pandas DataFrame back.
dataframe = pd.read_csv('BergenWeather2019.csv')

# Get the 'MinTemp' and 'MaxTemp' columns into a NumPy 2D array of shape (365,2).
temps = dataframe[['MinTemp', 'MaxTemp']].to_numpy()
print('temps shape', temps.shape)
print('temps dtype', temps.dtype)
print(temps)

# Determine the average in column 0 (min temps) and the average in column 1 (max temsp).
mean_mintemp = round(np.mean(temps[:, 0]), 1)
mean_maxtemp = round(np.mean(temps[:, 1]), 1)
print('Mean min temp:', mean_mintemp)
print('Mean max temp:', mean_maxtemp)

# Create a NumPy 1D array of shape (2,), containing averages for min and max temps.
mean_mintemp_maxtemp = np.array([mean_mintemp, mean_maxtemp])
print('Array containing mean min and mean max temps:', mean_mintemp_maxtemp)
print('Shape:', mean_mintemp_maxtemp.shape)

# Make use of NumPy "broadcasting" to do maths on arrays of shapes (52,2) and (2,).  
print('\nMinTemp relative to mean_mintemp, and MaxTemp relative to mean_maxtemp:\n', temps - mean_mintemp_maxtemp)