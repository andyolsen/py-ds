# Import the Pandas module.
import pandas as pd 

teams = ['Brazil', 'England', 'France', 'Italy', 'Spain', 'Uruguay', 'West Germany', 'Germany', 'Argentina']
wins  = [5, 1, 2, 4, 1, 2, 3, 1, 3]
stats = list(zip(teams,wins))
df = pd.DataFrame(stats, columns=['Team', 'Wins'])
df.index.name = 'Index'

# Write the DataFrame to a CSV file, with the Index and column headers.
df.to_csv('WorldCupWinners1.txt', index=True, header=True)

# Write the DataFrame to an Excel spreadsheet, with the Index and column headers.
df.to_excel('WorldCupWinners1.xlsx', index=True, header=True)

# Read the DataFrame back in again from a CSV file, recognising the embedded index and column headers.
df_from_csv1 = pd.read_csv('WorldCupWinners1.txt', index_col='Index', header=0)
print(df_from_csv1)

# Read the DataFrame back in again from an Excel spreadsheet, recognising the embedded index and column headers.
df_from_excel1 = pd.read_excel('WorldCupWinners1.xlsx', index_col='Index', header=0)
print(df_from_excel1)