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

# Slice rows.
print('\nandy and jayne\n',   df['andy' : 'jayne'])          
print('\nem onwards\n',       df['em':])          
print('\nup to em\n',         df[:'em'])          
print('\nup to em, step 2\n', df[:'em':2])          
print('\nall, step 2\n',      df[::2])          

# Mask rows.
print('\n170cm or taller\n', df[df['Height'] >= 170])          
print('\n60kg or lighter\n', df[df.Weight <= 60.0])          