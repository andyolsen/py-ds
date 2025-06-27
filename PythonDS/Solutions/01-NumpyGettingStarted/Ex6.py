import numpy as np
import pandas as pd

# Read a CSV file, get a Pandas DataFrame back.
dataframe = pd.read_csv('BergenWeather2019.csv')
print('Dataframe shape', dataframe.shape)

# Get the 'Precipitation' column as 32-bit floats.
precipitation = np.array(dataframe['Precipitation'], dtype=np.float32)
print('precipitation shape', precipitation.shape)
print(precipitation)

# Create a view of the first 364 values and reshape as a 2D array of shape (52, 7).
weeks = precipitation[:364].reshape((52,7))
print('\nweeks shape', weeks.shape)
print(weeks)

# Split the 2D weeks array by rows for q1, q2, and q3+q4. 
q1, q2, q3q4 = np.split(weeks, [13, 26])
print('\nq1 shape', q1.shape)
print(q1)
print('\nq2 shape', q2.shape)
print(q2)
print('\nq3q4 shape', q3q4.shape)
print(q3q4)

# Split the 2D weeks array by columns for weekdays and weekends. 
weekdays, weekends = np.hsplit(weeks, [5])
print('\nweekdays shape', weekdays.shape)
print(weekdays)
print('\nweekends shape', weekends.shape)
print(weekends)

# Stack q1, q2, q3q4 vertically to get back 52 weeks.
combined_quarters = np.vstack([q1, q2, q3q4])
print('\ncombined_quarters shape', combined_quarters.shape)
print(combined_quarters)

# Stack weekdays and weekends horizontally to get back 52 weeks.
combined_weekdays_weekends = np.hstack([weekdays, weekends])
print('\ncombined_weekdays shape', combined_weekdays_weekends.shape)
print(combined_weekdays_weekends)