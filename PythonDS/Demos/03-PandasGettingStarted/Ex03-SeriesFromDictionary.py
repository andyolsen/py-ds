# Import the Pandas module. 
import pandas as pd

# Create a Series from a Python dictionary.
s = pd.Series({
        'andy': 3.12, 
        'jayne': 19.1, 
        'em': 2.7, 
        'tom': 2.7
})
         
# Use the Series.
print(s)
print('Use explicit index  ', s['jayne'])
print('Shape of Series data', s.shape)