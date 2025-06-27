# Import the Pandas module. 
import pandas as pd

# Create a Series for each column.
bornSeries   = pd.Series({'andy': 1964, 'jayne': 1965, 'em': 1997, 'tom': 1997})
heightSeries = pd.Series({'andy':  167, 'jayne':  170, 'em':  165})
weightSeries = pd.Series({'andy': 60.0, 'jayne': 65.0,             'tom': 70.0})

# Create a DataFrame from a bunch of Series objects.
df = pd.DataFrame({
      'Born':   bornSeries, 
      'Height': heightSeries,
      'Weight': weightSeries
})

# Use the DataFrame.
print(df)                    # Access the whole DataFrame.
print(df['Born'])            # Access the 'Born' column.
print(type(df['Born']))      # A column in actually a Pandas Series object.
print(df['Born']['andy'])    # Access a row in the Series object, by index.