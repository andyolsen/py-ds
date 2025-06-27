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

# Do a merge, explicitly telling it the columns to merge in left/right datasets. 
df3 = pd.merge(df1, df2, left_on='name', right_on='navn')
print('\ndf3\n', df3)

# Same again, but drop the duplicate name/navn info.
df4 = pd.merge(df1, df2, left_on='name', right_on='navn').drop('navn', axis=1)
print('\ndf4\n', df4)