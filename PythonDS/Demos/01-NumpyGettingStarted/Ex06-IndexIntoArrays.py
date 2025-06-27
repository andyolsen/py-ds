import numpy as np

# Create a 1D array, index into it, and modify elements.
a = np.array([0, 10, 20, 30, 40, 50, 60, 70])
print(a)
print(a[1])        # 10
print(a[-1])       # 70
a[1] = 111
print(a)

# Create a 2D array, index into it, and modify elements.
b = np.array([[0, 10, 20, 30], [40, 50, 60, 70]])
print(b)
print(b[0, 1])     # 10
print(b[0, -1])    # 30
print(b[-1, 1])    # 50
print(b[-1, -1])   # 70
b[0, 1] = 111
print(b)