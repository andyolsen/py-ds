import numpy as np

a = np.arange(49).reshape(7,7)

# Combine fancy indexing with regular indexing.
cidx = [1, 3, 5]
result1 = a[2, cidx]
print('result1.shape', result1.shape)
print('result1\n',     result1)

# Combine fancy indexing with slicing.
cidx = [1, 3, 5]
result2 = a[2:5, cidx]
print('\nresult2.shape', result2.shape)
print('result2\n',       result2)

# Combine fancy indexing with slicing.
rmask = [True, True, False, False, False, False, True]
cidx = [1, 3, 5]
result3 = a[rmask, cidx]
print('\nresult3.shape', result3.shape)
print('result3\n',       result3)