import numpy as np

a = np.random.randint(0, 101, 12)
print('Unsorted 1D array', a)
print('Sorted           ', np.sort(a))

b = np.random.randint(0, 101, 49).reshape((7,7))
print('\nUnsorted 2D array\n', b)
print('\nSorted across cols\n', np.sort(b, axis=1))
print('\nSorted down rows  \n', np.sort(b, axis=0))