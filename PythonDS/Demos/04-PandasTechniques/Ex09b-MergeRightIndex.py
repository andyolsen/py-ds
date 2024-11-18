import pandas as pd

df1 = pd.DataFrame({
    'name':   ['Andy', 'Jayne', 'Em', 'Tom'],
    'born':   [1964, 1965, 1997, 1997]
})

df2 = pd.DataFrame({
    'navn':   ['Andy', 'Jayne', 'Em', 'Tom'],
    'height': [167, 170, 165, 177],
    'weight': [60.0, 65.0, 58.0, 70.0]          
})
df2 = df2.set_index('navn')

# Do a merge, telling it to use the 'name' column in the LHS dataset, and the index in the RHS dataset. 
df3 = pd.merge(df1, df2, left_on='name', right_index=True)
print('\ndf3\n', df3)