# Import the NumPy module. 
import numpy as np

# Create array with mixed types - NumPy converts element types "upwards".
a = np.array([1, 2, 3.14])
print('Data values in a\n', a)
print('Data type in a:', a.dtype)

# Create array with a specified type.
b = np.array([1, 2, 3], dtype='float64')
print('\nData values in b\n', b)
print('Data type in b:', b.dtype)

# Create array from a numeric range.
c = np.arange(0, 20, 2)
print('\nData values in c\n', c)
print('Data type in c:', c.dtype)

# Create array of 11 elements, linear spaced between 0 and 1 inclusive.
d = np.linspace(0.0, 1.0, 11)
print('\nData values in d\n', d)
print('Data type in d:', d.dtype)

# Create array of 5 zeros. 
# You can specify a tuple of dimensions for all the following examples, e.g. np.zeros((2,3)).
e = np.zeros(5)   
print('\nData values in e\n', e)
print('Data type in e:', e.dtype)

# Create array of 5 ones.
f = np.ones(5)   
print('\nData values in f\n', f)
print('Data type in f:', f.dtype)

# Create array of 5 elements with specified value.
g = np.full(5, 1.23)
print('\nData values in g\n', g)
print('Data type in g:', g.dtype)

# Create array of 5 elements with whatever values are in that memory.
h = np.empty(5)
print('\nData values in h\n', h)
print('Data type in h:', h.dtype)