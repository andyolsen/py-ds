import numpy as np
import pandas as pd

# Read a CSV file, get a Pandas DataFrame back.
dataframe = pd.read_csv('BergenWeather2019.csv')

# Get the 'MinTemp' and 'MaxTemp' columns into a NumPy array of shape (365,2).
temps = dataframe[['MinTemp', 'MaxTemp']].to_numpy()
print('temps shape', temps.shape)
print('temps dtype', temps.dtype)
print(temps)