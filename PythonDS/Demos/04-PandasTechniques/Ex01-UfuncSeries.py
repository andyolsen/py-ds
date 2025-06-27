import pandas as pd

stats = [ 
    {'born': 1964, 'height': 167, 'weight': 60.0},
    {'born': 1965, 'height': 170, 'weight': 65.0}, 
    {'born': 1997, 'height': 165, 'weight': 58.0}, 
    {'born': 1997, 'height': 177, 'weight': 70.0}
]
df = pd.DataFrame(stats, index=['andy', 'jayne', 'em', 'tom'])

# Perform ufunc on DataFrame column (i.e. Series), to convert height from cm to m.
df['height'] /= 100

# Perform ufunc on DataFrame column (i.e. Series), to create a new column.
df['weight_lbs'] = df['weight'] * 2.20462

# Also rename some columns, while we're at it.
df= df.rename(columns={'weight': 'weight_kg', 'height': 'height_m'})

print(df)