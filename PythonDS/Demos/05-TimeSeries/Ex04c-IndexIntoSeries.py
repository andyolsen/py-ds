import pandas as pd
from datetime import datetime

# Load data, and convert the MonthYear column into a DateTime type (for easier date-related processing).
data = pd.read_csv('Sales.csv', 
                    parse_dates=['MonthYear'], 
                    index_col='MonthYear',
                    date_format='%m/%Y')

# Get the SalesPerMonth column as a Pandas Series object.
ts = data['SalesPerMonth']

# Index into the Series object, specifying just the start of a range.
salesHalfTwo2019     = ts['2019-07-01' : ]
salesQuarterFour2019 = ts[datetime(2019,10,1) : ]

print('\nSales in H2 2019:\n', salesHalfTwo2019)
print('\nSales in Q4 2019:\n', salesQuarterFour2019)