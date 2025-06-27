import pandas as pd 

teams = ['Brazil', 'England', 'France', 'Italy', 'Spain', 'Uruguay', 'West Germany', 'Germany', 'Argentina']
wins  = [5, 1, 2, 4, 1, 2, 3, 1, 3]
stats = list(zip(teams,wins))
df = pd.DataFrame(stats, columns=['Team', 'Wins'])
df.index.name = 'Index'

# Print info about the DataFrame.
print('\nIndex:\n',        df.index)
print('\nTeam column:\n',  df['Team'])
print('\nWins column:\n',  df.Wins)
print('\nSummary info:\n', df.describe())