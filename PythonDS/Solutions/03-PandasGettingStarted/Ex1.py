# Import the Pandas module.
import pandas as pd 

# List of all the World Cup winners.
teams = ['Brazil', 'England', 'France', 'Italy', 'Spain', 'Uruguay', 'West Germany', 'Germany', 'Argentina']

# How many times each country has won the cup (e.g. Brazil have won the World Cup 5 times).
wins  = [5, 1, 2, 4, 1, 2, 3, 1, 3]

# Create a list of tuples. Each tuple is a (team, wins) pair.
stats = list(zip(teams,wins))

# Create a Pandas DataFrame with columns named 'Team', 'Wins'.
df = pd.DataFrame(stats, columns=['Team', 'Wins'])
print(df)

# Set the name of the index, for convenience.
df.index.name = 'Index'
print(df)