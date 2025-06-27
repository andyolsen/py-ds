import pandas as pd

# Load data, and convert the MonthYear column into a DateTime type (for easier date-related processing).
data = pd.read_csv('Sales.csv', 
                    parse_dates=['MonthYear'], 
                    index_col='MonthYear',
                    date_format='%m/%Y')

print('\nParsed data\n', data.head())
print('\nData types\n', data.dtypes)
print('\nData index\n', data.index)