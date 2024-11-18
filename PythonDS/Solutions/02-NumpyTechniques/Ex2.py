import numpy as np
import pandas as pd

# Read a CSV file, get a Pandas DataFrame back, and assign the 'Precipitation' column to a NumPy array.
dataframe = pd.read_csv('BergenWeather2019.csv')
precipitation_mm = np.array(dataframe['Precipitation'])
precipitation_inches_4dp = np.around(precipitation_mm / (10 * 2.54), 4)
print('\nPrecipitation inches to 4dp\n', precipitation_inches_4dp)

print('Total annual precipitation:    ', round(np.sum(precipitation_inches_4dp), 4))
print('Minimum precipitation on a day:', np.min(precipitation_inches_4dp))
print('Maximum precipitation on a day:', np.max(precipitation_inches_4dp))
print('Mean daily precipitation:      ', round(np.mean(precipitation_inches_4dp), 4))
print('Median daily precipitation:    ', round(np.median(precipitation_inches_4dp), 4))
print('Variance:                      ', round(np.var(precipitation_inches_4dp), 4))
print('Standard deviation:            ', round(np.std(precipitation_inches_4dp), 4))
print('1st quartile:                  ', np.percentile(precipitation_inches_4dp, 25))
print('2nd quartile:                  ', np.percentile(precipitation_inches_4dp, 50))
print('3rd quartile:                  ', np.percentile(precipitation_inches_4dp, 75))