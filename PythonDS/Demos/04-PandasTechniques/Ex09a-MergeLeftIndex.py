import pandas as pd

df1 = pd.DataFrame({
    'name':   ['Andy', 'Jayne', 'Em', 'Tom'],
    'born':   [1964, 1965, 1997, 1997]
})
df1 = df1.set_index('name')

df2 = pd.DataFrame({
    'navn':   ['Andy', 'Jayne', 'Em', 'Tom'],
    'height': [167, 170, 165, 177],
    'weight': [60.0, 65.0, 58.0, 70.0]          
})

# Do a merge, telling it to use the index in the LHS dataset. 
df3 = pd.merge(df1, df2, left_index=True, right_on='navn')
print('\ndf3\n', df3)