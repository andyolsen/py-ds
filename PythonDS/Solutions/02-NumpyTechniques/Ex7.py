import numpy as np
import pandas as pd

# Read a CSV file, get a Pandas DataFrame back, and assign the 'Precipitation' column to a NumPy array.
dataframe = pd.read_csv('BergenWeather2019.csv')
precipitation = np.array(dataframe['Precipitation'])
precipitation = np.around(precipitation / (10 * 2.54), 4)
print('\nPrecipitation inches to 4dp\n', precipitation)

# Use a Boolean mask on a NumPy array, to get an array of days of precipitation.
days_of_precipitation = precipitation[precipitation > 0]
print('\nNumber of days of precipitation:   ', days_of_precipitation.size)
print('Number of days of no precipitation:', precipitation.size - days_of_precipitation.size)
print('\nPrecipitation amounts:\n', days_of_precipitation)

# Compare the mean daily precipitation all year, with that of rainy days only.
print('\nMean daily precipitation all year:  ', round(np.mean(precipitation), 4))
print('Mean of rainy days only:            ',   round(np.mean(days_of_precipitation), 4))

# Compare the median daily precipitation all year, with that of rainy days only.
print('\nMedian daily precipitation all year:', round(np.median(precipitation), 4))
print('Median of rainy days only:          ',   round(np.median(days_of_precipitation), 4))

# Compare the variance of daily precipitation all year, with that of rainy days only.
print('\nVariance all year:                  ', round(np.var(precipitation), 4))
print('Variance of rainy days only:        ',   round(np.var(days_of_precipitation), 4))

# Compare the standard deviation of daily precipitation all year, with that of rainy days only.
print('\nStd dev all year:                   ', round(np.std(precipitation), 4))
print('Std dev of rainy days only:         ',   round(np.std(days_of_precipitation), 4))