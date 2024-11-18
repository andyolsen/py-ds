import pandas as pd
from datetime import datetime

# Load data, and convert the MonthYear column into a DateTime type (for easier date-related processing).
data = pd.read_csv('Sales.csv', 
                    parse_dates=['MonthYear'], 
                    index_col='MonthYear',
                    date_format='%m/%Y')

# Get the SalesPerMonth column as a Pandas Series object.
ts = data['SalesPerMonth']

# Index into the Series object, to get a range of items from the series.
salesQuarterOne2009 = ts['2009-01-01' : '2009-03-01']
salesQuarterTwo2009 = ts[datetime(2009,4,1) : datetime(2009,6,1)]

print('\nSales in Q1 2009:\n', salesQuarterOne2009)
print('\nSales in Q2 2009:\n', salesQuarterTwo2009)