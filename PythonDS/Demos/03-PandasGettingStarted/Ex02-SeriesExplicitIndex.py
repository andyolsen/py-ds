# Import the Pandas module. 
import pandas as pd

# Create a Series with values and explicit index.
s = pd.Series([3.12, 19.1, 2.7, 2.7],
              index=['andy', 'jayne', 'em', 'tom'])

# Use the Series.
print(s)
print('Use explicit index  ', s['jayne'])
print('Shape of Series data', s.shape)