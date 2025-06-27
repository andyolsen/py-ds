import numpy as np
import pandas as pd

# Read a CSV file, get a Pandas DataFrame back, and assign the 'Precipitation' column to a NumPy array.
dataframe = pd.read_csv('BergenWeather2019.csv')
precipitation_mm = np.array(dataframe['Precipitation'])
print('\nPrecipitation mm\n', precipitation_mm)

precipitation_cm = precipitation_mm / 10
print('\nPrecipitation cm\n', precipitation_cm)

precipitation_inches = precipitation_cm / 2.54
print('\nPrecipitation inches\n', precipitation_inches)

precipitation_inches_4dp = np.around(precipitation_inches, 4)
print('\nPrecipitation inches to 4dp\n', precipitation_inches_4dp)