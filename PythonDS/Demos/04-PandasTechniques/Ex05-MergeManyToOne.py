import pandas as pd

df1 = pd.DataFrame({
    'name':   ['Andy', 'Jayne', 'Em', 'Tom'],
    'office': ['SWA', 'SWA', 'MCR', 'LON']
})

df2 = pd.DataFrame({
    'office':  ['SWA', 'LON', 'MCR', 'ABD'],
    'city':    ['Swansea', 'London', 'Manchester', 'Aberdeen'],
    'region':  ['Wales', 'S England', 'N England', 'Scotland']          
})

# Do a many-to-one merge, based on the common 'office' column. 
df3 = pd.merge(df1, df2)
print('\ndf3\n', df3)