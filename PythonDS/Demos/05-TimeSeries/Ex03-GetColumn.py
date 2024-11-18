import pandas as pd

# Load data, and convert the MonthYear column into a DateTime type (for easier date-related processing).
data = pd.read_csv('Sales.csv', 
                    parse_dates=['MonthYear'], 
                    index_col='MonthYear',
                    date_format='%m/%Y')

# Get the SalesPerMonth column as a Pandas Series object.
ts = data['SalesPerMonth']

print('\nSalesPerMonth as a Pandas Series data\n', ts.head())