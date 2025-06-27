import numpy as np
import pandas as pd

coords = [ 
    {'x': 1, 'y': 2}, {'x': 3, 'y': 4}, {'x': 5, 'y': 6}
]
df = pd.DataFrame(coords)

print('df + 2\n',  df + 2)
print('df - 2\n',  df - 2)
print('df * 2\n',  df * 2)
print('df / 2\n',  df / 2)
print('df // 2\n', df // 2)
print('df % 2\n',  df % 2)
print('df ** 2\n', df ** 2)

print('sin(df)\n',  np.sin(df))
print('cos(df)\n',  np.cos(df))
print('tan(df)\n',  np.tan(df))
print('sinh(df)\n', np.sinh(df))
print('cosh(df)\n', np.cosh(df))
print('tanh(df)\n', np.tanh(df))