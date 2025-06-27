# Import the Pandas module. 
import pandas as pd

# Create a Series with values and implicit index.
s = pd.Series([3.12, 19.1, 2.7, 2.7])

# Use the Series.
print(s)
print('Use implicit index  ', s[0])
print('Shape of Series data', s.shape)