import numpy as np
import pandas as pd

# Read a CSV file, get a Pandas DataFrame back.
dataframe = pd.read_csv('WorldCupWinners.csv')

# Get the 'Team' column.
teams = np.array(dataframe['Team'])
print(teams)