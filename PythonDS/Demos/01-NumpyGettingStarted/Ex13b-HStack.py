import numpy as np

# Create some arrays with same number of rows (2), and stack horizontally.
c = np.array([[40, 41], [50, 51]])
d = np.array([[60], [61]])
result2 = np.hstack([c, d])
print(result2)         # [[40 41 60] [50 51 61]]
print(result2.shape)   # (2, 3) 