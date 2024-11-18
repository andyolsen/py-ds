import pandas as pd

df1 = pd.DataFrame({
    'name':   ['Andy', 'Jayne', 'Em', 'Tom'],
    'salary': [10000, 20000, 30000, 40000]
})
df1 = df1.set_index('name')

df2 = pd.DataFrame({
    'name':  ['Andy', 'Jayne', 'Gareth'],
    'level': ['Medium', 'Expert', 'Genius'],
    'years': [3, 5, 20]          
})
df2 = df2.set_index('name')

# Do a right join.
df3 = pd.merge(df1, df2, left_index=True, right_index=True, how='right')
df3.index.name = 'name'
print('\ndf3\n', df3)