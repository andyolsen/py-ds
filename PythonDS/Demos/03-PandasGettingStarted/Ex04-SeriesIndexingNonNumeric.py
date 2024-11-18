# Import the Pandas module. 
import pandas as pd

# Create a Series where the index is non-numeric.
data = pd.Series(['John', 'Mary', 'Emma', 'Alex', 'Jeff'],
                 index=['E100', 'E101', 'E257', 'E118', 'E123'])

print(data)

# You can access elements via explicit index.
print('\nIndexing via explicit index\n', data['E101'])     
print('Slicing via explicit index\n',    data['E101':'E118'])  # Inclusive of end element.   

# You can also access elements via implicit index, i.e. row number.
print('\nIndexing via implicit index\n', data[1])     
print('Slicing via implicit index\n',    data[1:3])            # Exclusive of end element.