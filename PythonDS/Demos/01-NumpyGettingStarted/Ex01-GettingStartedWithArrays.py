# Import the NumPy module. 
import numpy as np

# Create a 1D NumPy array from a Python list.
a = np.array([1, 2, 3])
print('Data values in a\n', a)
print('Shape of a:', a.shape)
print('Data type in a:', a.dtype)

# Create a 2D NumPy array from a Python list of lists.
b = np.array([[1, 2, 3], [4, 5, 6]])
print('\nData values in b\n', b)
print('Shape of b:', b.shape)
print('Data type in b:', b.dtype)