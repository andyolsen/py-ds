import numpy as np
import pandas as pd

coords = [ 
  {'x': 1, 'y': 2}, {'x': 3, 'y': 4}, {'x': 5, 'y': 6}
]
df = pd.DataFrame(coords)
s  = pd.Series({'x': 100, 'y': 200})

print('Using operators')
print('df + s\n',  df + s)
print('df - s\n',  df - s)
print('df * s\n',  df * s)
print('df / s\n',  df / s)
print('df // s\n', df // s)
print('df % s\n',  df % s)
print('df ** s\n', df ** s)