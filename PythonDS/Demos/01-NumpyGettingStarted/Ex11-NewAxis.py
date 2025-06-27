import numpy as np

# Create 1D array initially, for simplicity.
a = np.arange(5)
print(a)               # [0 1 2 3 4]
print(a.shape)         # (5,)

# Create 2D array with 1 row, 5 columns. 
b = a[np.newaxis, :]   
print(b)               # [[0 1 2 3 4]]
print(b.shape)         # (1, 5)

# Create 2D array with 5 rows, 1 column. 
c = a[:, np.newaxis]   
print(c)               # [[0] [1] [2] [3] [4]]
print(c.shape)         # (5, 1)