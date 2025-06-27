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

# Index into columns.
print('\nBorn\n',            df['Born'])               # Use [] notation to get 1 column, as a Series.          
print('\nHeight, Weight\n',  df[['Height', 'Weight']]) # Use [] notation to get multiple columns, as a DataFrame.
print('\nBorn\n',            df.Born)                  # Use property notation to get 1 column.

# Create a new column.
df['BMI'] = df['Weight'] / ((df['Height']/100.0) ** 2)        
print('\nBMI calculation\n', df['BMI'])