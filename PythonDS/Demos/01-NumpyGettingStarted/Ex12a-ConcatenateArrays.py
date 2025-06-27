import numpy as np

# Create some 1D arrays.
a = np.array([ 0,  1])
b = np.array([10, 11])
c = np.array([20, 21])

# Concatenate the 1D arrays.
result = np.concatenate([a, b, c])
print(result)         # [0 1 10 11 20 21]
print(result.shape)   # (6,) 