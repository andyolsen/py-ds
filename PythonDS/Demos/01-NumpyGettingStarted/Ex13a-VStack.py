import numpy as np

# Create some arrays with same number of columns (2), and stack vertically.
a = np.array([10, 11])
b = np.array([[20, 21], [30, 31]])
result1 = np.vstack([a, b])
print(result1)         # [[10 11] [20 21] [30 31]]
print(result1.shape)   # (3, 2)      