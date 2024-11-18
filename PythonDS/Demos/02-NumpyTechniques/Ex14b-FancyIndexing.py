import numpy as np

a = np.arange(49).reshape(7,7)

# Use fancy indexing to specify rows and columns desired.
ridx = [0, 2, 4]
cidx = [1, 3, 5]
result = a[ridx, cidx]
print('result.shape', result.shape)
print('result      ', result)