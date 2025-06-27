import numpy as np
import pandas as pd

# Read a CSV file, get a Pandas DataFrame back.
dataframe = pd.read_csv('BergenWeather2019.csv')
print('Dataframe shape', dataframe.shape)

# Get the 'Precipitation' column.
precipitation = np.array(dataframe['Precipitation'])
print('precipitation shape', precipitation.shape)
print('precipitation dtype', precipitation.dtype)
print(precipitation)