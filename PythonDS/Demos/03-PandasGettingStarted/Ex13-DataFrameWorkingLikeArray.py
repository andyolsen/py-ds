# Import the Pandas module. 
import pandas as pd

# Create a Series for each column.
bornSeries   = pd.Series({'andy': 1964, 'jayne': 1965, 'em': 1997, 'tom': 1997})
heightSeries = pd.Series({'andy':  167, 'jayne':  170, 'em':  165, 'tom':  177})
weightSeries = pd.Series({'andy': 60.0, 'jayne': 65.0, 'em': 58.0, 'tom': 70.0})

# Create a DataFrame from a bunch of Series objects.
df = pd.DataFrame({
      'Born':   bornSeries, 
      'Height': heightSeries,
      'Weight': weightSeries
})

# Use .loc to treat like 2D array, specifying [row-indexer-by-name, col-indexer-by-name].
print('\nem onwards, all columns\n',           df.loc['em':])                               # Slice
print('\nandy and jayne, height and weight\n', df.loc['andy':'jayne', 'Height':'Weight'])   # Slice
print('\nandy and tom, born and height\n',     df.loc[['andy','tom'], ['Born', 'Height']])  # Fancy indexing        
print('\n170cm or taller, height\n',           df.loc[df['Height'] >= 170, 'Height'])       # Mask

# Use .iloc to treat like 2D array, specifying [row-indexer-by-number, col-indexer-by-number].
print('\nem onwards, all columns\n',           df.iloc[2:])              # Slice 
print('\nandy and jayne, height and weight\n', df.iloc[0:2, 1:3])        # Slice, exclusive end element.
print('\nandy and tom, born and height\n',     df.iloc[[0,3], [0, 1]])   # Fancy indexing        