import numpy as np
import pandas as pd

# Read an Excel spreadsheet, get a Pandas DataFrame back.
dataframe = pd.read_excel('BergenWeather2019.xlsx')
print('dataframe shape', dataframe.shape)

# Get the 'Precipitation' column.
precipitation = np.array(dataframe['Precipitation'])
print('precipitation shape', precipitation.shape)
print('precipitation dtype', precipitation.dtype)
print(precipitation)