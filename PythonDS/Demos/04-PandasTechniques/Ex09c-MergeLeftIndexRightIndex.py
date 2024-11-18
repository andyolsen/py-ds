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
df2 = df2.set_index('navn')

# Do a merge, telling it to use the index in both LHS and RHS datasets. 
df3 = pd.merge(df1, df2, left_index=True, right_index=True)
df3.index.name = 'nom'
print('\ndf3\n', df3)

# Equivalently, call join(), which implicitly joins the datasets by index. 
df4 = df1.join(df2)
df4.index.name = 'enw'
print('\ndf4\n', df4)