# Import the NumPy module. 
import numpy as np

# Create 10 random values in range [0.0, 1.0).
a = np.random.random(10)
print('Data values in a\n', a)
print('Data type in a:', a.dtype)

# Create 10 normally-distributed random values, arithmetic mean 5, standard deviation 2.
b = np.random.normal(5, 2, 10)
print('\nData values in b\n', b)
print('Data type in b:', b.dtype)

# Create 10 random integers in range [0, 101).
c = np.random.randint(0, 101, 10)
print('\nData values in c\n', c)
print('Data type in c:', c.dtype)