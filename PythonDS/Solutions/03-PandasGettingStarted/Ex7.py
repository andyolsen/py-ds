import pandas as pd 

teams = ['Brazil', 'England', 'France', 'Italy', 'Spain', 'Uruguay', 'West Germany', 'Germany', 'Argentina']
wins  = [5, 1, 2, 4, 1, 2, 3, 1, 3]
stats = list(zip(teams,wins))
df = pd.DataFrame(stats, columns=['Team', 'Wins'])
df.index.name = 'Index'

# Add a column for year of first win.
df['YearFirstWin'] = pd.Series([1958, 1966, 1998, 1934, 2010, 1930, 1954, 2014, 1978])
print(df)

# Work with rows.
print('\nOne-time winners:\n', df[df.Wins == 1])
print('\nMultiple winners:\n', df[df.Wins > 1])
print('\nFirst win this millennium:\n',  df[df.YearFirstWin >= 2000])
print('\nTwice or thrice winners:\n',    df[(df.Wins == 2) | (df.Wins == 3)])
print('\nTwice or thrice team names:\n', df[(df.Wins == 2) | (df.Wins == 3)].Team)