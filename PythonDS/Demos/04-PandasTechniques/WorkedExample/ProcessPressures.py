import pandas as pd 

# Read text file (using TAB as separator, skip first 10 rows, and treat next row as header). 
df = pd.read_csv('Pressures.txt', sep='\t', skiprows=10, header=0)
print('\nWhole DataFrame:\n', df)
print('\nShape of DataFrame:', df.shape)

# Get a pointer to the TimeStamp column.
timeStamp_column = pd.to_datetime(df['TimeStamp'])
print('\nTimeStamp column:\n', timeStamp_column)
print('\nShape of TimeStamp column:', timeStamp_column.shape)

# Calculate time deltas between adjacent rows in TimeStamp column (in seconds), 
# and put these time deltas into a new column named TimeStampDifference in the DataFrame.
df['TimeStampDifference'] = timeStamp_column.diff().dt.seconds
print(df['TimeStampDifference'])

# For info, what's the frequency of the time deltas?
difference_value_counts = df['TimeStampDifference'].value_counts()
print('\nDifferences counts:\n', difference_value_counts)

# Get the rows where the TimeStampDifference is 1 second, and save to Excel.
diffs_1sec = df[df.TimeStampDifference == 1]
print('1-second differences:\n', diffs_1sec)
diffs_1sec.to_excel('Differences_1sec.xlsx')

# Get the rows where the TimeStampDifference is 5 seconds, and save to Excel.
diffs_5sec = df[df.TimeStampDifference == 5]
print('5-second differences:\n', diffs_5sec)
diffs_5sec.to_excel('Differences_5sec.xlsx')

# Get the rows where the TimeStampDifference is not 1 or 5 seconds, and save to Excel.
diffs_other = df[(df.TimeStampDifference != 1) & (df.TimeStampDifference != 5)]
print('Other differences:\n', diffs_other)
diffs_other.to_excel('Differences_Other.xlsx')