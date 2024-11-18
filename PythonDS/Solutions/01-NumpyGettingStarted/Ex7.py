import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read a csv file, get a Pandas DataFrame back.
dataframe = pd.read_csv('BergenWeather2019.csv')
print('Dataframe shape', dataframe.shape)

# Get the 'Precipitation' column as 32-bit floats.
precipitation = np.array(dataframe['Precipitation'], dtype=np.float32)
print('precipitation shape', precipitation.shape)
print('precipitation dtype', precipitation.dtype)
print(precipitation)

# Define a dictionary of font properties for the title.
fontdict = {
    'fontfamily': 'Courier New', 
    'fontsize': 16, 
    'color': 'green', 
    'fontweight': 'bold'}

# Draw the precipitation as a plot (i.e. graph).
plt.xlabel('Day of year')
plt.ylabel('Precipitation [mm]')
plt.title('Precipitation in Bergen 2019', fontdict)           
plt.plot(precipitation)
plt.show()

# Draw the precipitation as a barchart.
plt.xlabel('Day of year')
plt.ylabel('Precipitation [mm]')
plt.title('Precipitation in Bergen 2019', fontdict)           
plt.bar(np.arange(precipitation.size), precipitation)
plt.show()

# Now draw a histogram to show the precipitation frequency.
plt.xlabel('Precipitation [mm]')
plt.ylabel('Number of days')
plt.title('Precipitation frequency in Bergen 2019', fontdict)           
plt.hist(precipitation, bins=10)
plt.show()