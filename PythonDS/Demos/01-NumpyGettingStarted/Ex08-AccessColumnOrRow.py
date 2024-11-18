import numpy as np

a = np.array([[0, 10, 20], [30, 40, 50], [60, 70, 80]])

# To access a specific column...
print(a[:, 0])   # [ 0 30 60]
print(a[:, 1])   # [10 40 70]
print(a[:, 2])   # [20 50 80]

# To access a specific row...
print(a[0, :])   # [ 0 10 20]
print(a[1, :])   # [30 40 50]
print(a[2, :])   # [60 70 80]

# To access a specific row, simpler syntax...
print(a[0])      # [ 0 10 20]
print(a[1])      # [30 40 50]
print(a[2])      # [60 70 80]