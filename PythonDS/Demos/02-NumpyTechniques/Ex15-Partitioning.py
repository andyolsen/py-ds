import numpy as np

a = np.random.randint(0, 101, 12)
print('Unpartitioned 1D array', a)
print('Partitioned at index 2', np.partition(a, 2))
print('Partitioned at index 4', np.partition(a, 4))

b = np.random.randint(0, 101, 49).reshape((7,7))
print('\nUnpartitioned 2D array\n', b)
print('\nPartitioned at col index 2\n', np.partition(b, 2, axis=1))
print('\nPartitioned at col index 4\n', np.partition(b, 4, axis=1))
print('\nPartitioned at row index 2\n', np.partition(b, 2, axis=0))
print('\nPartitioned at row index 4\n', np.partition(b, 4, axis=0))