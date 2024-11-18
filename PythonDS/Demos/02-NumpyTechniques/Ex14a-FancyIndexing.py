import numpy as np

a = np.arange(10, 20)

# Get some elements into a Python list.
result1 = [a[1], a[4], a[7]]
print('type(result1)', type(result1))
print('result1      ', result1)

# Get some elements into a NumPy array, using fancy indexing.
indexes = [1, 4, 7]
result2 = a[indexes]
print('\ntype(result2)', type(result2))
print('result2.shape',   result2.shape)
print('result2      ',   result2)

# Get some elements into a 2D NumPy array, using fancy indexing.
indexes = np.array([[1, 4, 7], [2, 5, 8]])
result3 = a[indexes]
print('\ntype(result3)', type(result3))
print('result3.shape',   result3.shape)
print('result3      ',   result3)