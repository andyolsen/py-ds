# Import the Pandas module. 
import pandas as pd

stats = [ 
    {'born': 1964, 'height': 167, 'weight': 60.0},
    {'born': 1965, 'height': 170, 'weight': 65.0}, 
    {'born': 1997, 'height': 165, 'weight': 58.0}, 
    {'born': 1997, 'height': 177, 'weight': 70.0}
]

names = ['andy', 'jayne', 'em', 'tom']

# Create a DataFrame with specified data and index.
df = pd.DataFrame(data=stats, index=names)

# Use the DataFrame.
print(df)                    # Access the whole DataFrame.
print(df['born'])            # Access the 'born' column.
print(type(df['born']))      # A column in actually a Pandas Series object.
print(df['born']['andy'])    # Access a row in the Series object, by index.