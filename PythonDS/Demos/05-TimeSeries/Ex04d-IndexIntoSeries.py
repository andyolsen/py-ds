import pandas as pd
from datetime import datetime

# Load data, and convert the MonthYear column into a DateTime type (for easier date-related processing).
data = pd.read_csv('Sales.csv', 
                    parse_dates=['MonthYear'], 
                    index_col='MonthYear',
                    date_format='%m/%Y')

# Get the SalesPerMonth column as a Pandas Series object.
ts = data['SalesPerMonth']

# Index into the Series object, specifying just the end of a range.
salesHalfOne2009    = ts[ : '2009-06-01']
salesQuarterOne2009 = ts[ : datetime(2009,3,1) ]

print('\nSales in H1 2009:\n', salesHalfOne2009)
print('\nSales in Q1 2009:\n', salesQuarterOne2009)