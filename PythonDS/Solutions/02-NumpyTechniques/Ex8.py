import numpy as np
import pandas as pd

# Read a CSV file, get a Pandas DataFrame back, and assign the 'Precipitation' column to a NumPy array.
dataframe = pd.read_csv('BergenWeather2019.csv')
precipitation = np.array(dataframe['Precipitation'])
precipitation = np.around(precipitation / (10 * 2.54), 4)
print('\nPrecipitation inches to 4dp\n', precipitation)

days_of_precipitation = precipitation[precipitation > 0]
print('\nPrecipitation amounts:\n', days_of_precipitation)

# Use fancy indexing to pluck out the first and last days of precipitation.
first_last_wet_days = [0, -1]
precipitation_first_last_wet_days = days_of_precipitation[first_last_wet_days]
print('\nPrecipitation on first and last wet days:', precipitation_first_last_wet_days)

# Partition the rainy days into the 30 least wet days, then the rest.
print('\nPrecipitation partitioned at 30:\n',   np.partition(days_of_precipitation, 30))

# Sort the rainy days.
print('\nPrecipitation in sorted order:\n', np.sort(days_of_precipitation))