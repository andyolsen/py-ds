import numpy as np
import pandas as pd

# Read a CSV file, get a Pandas DataFrame back.
dataframe = pd.read_csv('BergenWeather2019.csv')

# Get the 'MinTemp' and 'MaxTemp' columns into a NumPy 2D array of shape (365,2).
temps = dataframe[['MinTemp', 'MaxTemp']].to_numpy()
print('temps shape', temps.shape)
print('temps dtype', temps.dtype)
print(temps)

# Work with a multidimensional NumPy array.
diurnal_ranges = temps[:, 1] - temps[:, 0]
print('\nDiurnal temperature ranges:\n', diurnal_ranges)
print('\nDiurnal temperature range > 8.0?\n', diurnal_ranges > 8.0)
print('\nDiurnal temperature range < 4.0?\n', diurnal_ranges < 4.0)