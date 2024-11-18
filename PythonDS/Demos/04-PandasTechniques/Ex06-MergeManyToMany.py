import pandas as pd

df1 = pd.DataFrame({
    'name': ['Andy', 'Jayne', 'Em', 'Tom'],
    'region': ['Wal', 'Wal', 'NEng', 'SEng']
})

df2 = pd.DataFrame({
    'region': ['Wal', 'SEng', 'SEng', 'NEng', 'NEng'],
    'city':   ['Barry', 'Dover', 'Bath', 'York', 'Hull']
})

# Do a many-to-many merge, based on the common 'region' column. 
df3 = pd.merge(df1, df2)

# Bonus bit: Add a new column that indicates the first occurrence of a region.
df3['first_occurrence_of_region'] = df3.groupby('region').cumcount() == 0
print('\ndf3\n', df3)