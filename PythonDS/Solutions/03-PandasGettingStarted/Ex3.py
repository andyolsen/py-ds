# Import the Pandas module.
import pandas as pd 

teams = ['Brazil', 'England', 'France', 'Italy', 'Spain', 'Uruguay', 'West Germany', 'Germany', 'Argentina']
wins  = [5, 1, 2, 4, 1, 2, 3, 1, 3]
stats = list(zip(teams,wins))
df = pd.DataFrame(stats, columns=['Team', 'Wins'])
df.index.name = 'Index'

# Write the DataFrame to a CSV file, without the Index or column headers.
df.to_csv('WorldCupWinners2.txt', index=False, header=False)

# Write the DataFrame to an Excel spreadsheet, without the Index or column headers.
df.to_excel('WorldCupWinners2.xlsx', index=False, header=False)

# Read the DataFrame back in again from a CSV file, and reinstate the index and column names.
df_from_csv2 = pd.read_csv('WorldCupWinners2.txt', names=['Team', 'Wins'])
df_from_csv2.index.name = 'Index'
print(df_from_csv2)

# Read the DataFrame back in again from an Excel spreadsheet, and reinstate the index and column names.
df_from_excel2 = pd.read_excel('WorldCupWinners2.xlsx', names=['Team', 'Wins'])
df_from_excel2.index.name = 'Index'
print(df_from_excel2)