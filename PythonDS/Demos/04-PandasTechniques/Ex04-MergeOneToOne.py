import pandas as pd

df1 = pd.DataFrame({
    'name':   ['Andy', 'Jayne', 'Em', 'Tom'],
    'born':   [1964, 1965, 1997, 1997]
})

df2 = pd.DataFrame({
    'name':   ['Andy', 'Jayne', 'Em', 'Tom'],
    'height': [167, 170, 165, 177],
    'weight': [60.0, 65.0, 58.0, 70.0]          
})

# Do a one-to-one merge, based on the common 'name' column. 
df3 = pd.merge(df1, df2)
print('\ndf3\n', df3)