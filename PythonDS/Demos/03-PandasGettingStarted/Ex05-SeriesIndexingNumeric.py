# Import the Pandas module. 
import pandas as pd

# Create a Series where the index is numeric.
data = pd.Series(['John', 'Mary', 'Emma', 'Alex', 'Jeff'],
                 index=[100, 101, 257, 118, 123])

print(data)

# Using [] can be confusing!
print('\nIndexing uses explicit index\n',  data[101])     
print('But slicing uses implicit index\n', data[1:3])              # Exclusive of end element.

# .loc always uses explicit index.
print('\n.loc indexing uses explicit index\n', data.loc[101])     
print('.loc slicing uses explicit index\n',    data.loc[101:118])  # Inclusive of end element.  

# .iloc always uses implicit index.
print('\n.iloc indexing uses implicit index\n', data.iloc[1])     
print('.iloc slicing uses implicit index\n',    data.iloc[1:3])    # Exclusive of end element.  