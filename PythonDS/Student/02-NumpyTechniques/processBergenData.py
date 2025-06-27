import numpy as np
import pandas as pd

# Read a CSV file, get a Pandas DataFrame back, and assign the 'Precipitation' column to a NumPy array.
dataframe = pd.read_csv('BergenWeather2019.csv')
precipitation_mm = np.array(dataframe['Precipitation'])
print('\nPrecipitation mm\n', precipitation_mm)