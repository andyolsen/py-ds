import pandas as pd 

teams = ['Brazil', 'England', 'France', 'Italy', 'Spain', 'Uruguay', 'West Germany', 'Germany', 'Argentina']
wins  = [5, 1, 2, 4, 1, 2, 3, 1, 3]
stats = list(zip(teams,wins))
df = pd.DataFrame(stats, columns=['Team', 'Wins'])
df.index.name = 'Index'

# Add a column for year of first win.
df['YearFirstWin'] = pd.Series([1958, 1966, 1998, 1934, 2010, 1930, 1954, 2014, 1978])
print(df)