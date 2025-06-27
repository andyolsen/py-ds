import numpy as np
import pandas as pd

# Read a CSV file, get a Pandas DataFrame back.
dataframe = pd.read_csv('BergenWeather2019.csv')
print('Dataframe shape', dataframe.shape)

# Get the 'Precipitation' column as 32-bit floats.
precipitation = np.array(dataframe['Precipitation'], dtype=np.float32)
print('precipitation shape', precipitation.shape)
print('precipitation dtype', precipitation.dtype)
print(precipitation)

# Access specific elements.
print('precipitation on  1 Jan:', precipitation[0])
print('precipitation on  2 Jan:', precipitation[1])
print('precipitation on 31 Dec:', precipitation[-1])
print('precipitation on 30 Dec:', precipitation[-2])

# Access slice of  elements.
print('\nprecipitation in January:\n',     precipitation[:31])
print('\nprecipitation in December:\n',    precipitation[-31:])
print('\nprecipitation in November:\n',    precipitation[-61:-31])
print('\nprecipitation every 10th day:\n', precipitation[::10])