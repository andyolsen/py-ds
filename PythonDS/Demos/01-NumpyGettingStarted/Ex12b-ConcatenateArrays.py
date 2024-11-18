import numpy as np

# Create some 2D arrays.
a = np.array([[ 0,  1], [10, 11]])
b = np.array([[20, 21], [30, 31]])
c = np.array([[40, 41], [50, 51]])

# Concatenate on axis 0 (this is the default, so can omit axis parameter).
result1 = np.concatenate([a, b, c], axis=0)
print(result1)         # [[0 1] [10 11] [20 21] [30 31] [40 41] [50 51]]
print(result1.shape)   # (6, 2)      

# Concatenate on axis 1.
result2 = np.concatenate([a, b, c], axis=1)
print(result2)         # [[0 1 20 21 40 41] [10 11 30 31 50 51]]
print(result2.shape)   # (2, 6) 