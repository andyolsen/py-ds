import pandas as pd
from datetime import datetime

# Load data, and convert the MonthYear column into a DateTime type (for easier date-related processing).
data = pd.read_csv('Sales.csv', 
                    parse_dates=['MonthYear'], 
                    index_col='MonthYear',
                    date_format='%m/%Y')

# Get the SalesPerMonth column as a Pandas Series object.
ts = data['SalesPerMonth']

# Index into the Series object, using a datetime string or datetime object as an index. Gets the sales for that month.
salesFeb2009 = ts['2009-02-01']
salesMar2009 = ts[datetime(2009, 3, 1)]

print('Sales in Feb 2009:', salesFeb2009)
print('Sales in Mar 2009:', salesMar2009)