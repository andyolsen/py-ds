import numpy as np

# Create 1D array initially, for simplicity.
a = np.arange(9)
print(a)               # [0 1 2 3 4 5 6 7 8]
print(a.shape)         # (9,)

# Reshape as 2D array (view on a).
b = a.reshape((3,3))  
print(b)               # [[0 1 2] [3 4 5] [6 7 8]]
print(b.shape)         # (3, 3)

# Changing items in b will change values in underlying a.
b[0,0] = 99          
print(a)               # [99  1  2  3  4  5  6  7  8]
print(b)               # [[99  1  2] [ 3  4  5] [ 6  7  8]]