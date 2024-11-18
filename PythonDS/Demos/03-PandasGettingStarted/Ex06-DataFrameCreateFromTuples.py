import pandas as pd 

names = ['Andy', 'Jayne', 'Em', 'Tom']
born  = [1964, 1965, 1997, 1997]

# Create a list of tuples. Each tuple is a (names, born) pair.
stats = list(zip(names,born))

# Create a DataFrame with specified data and column names. 
df = pd.DataFrame(stats, columns=['Name', 'Born'])

print(df)