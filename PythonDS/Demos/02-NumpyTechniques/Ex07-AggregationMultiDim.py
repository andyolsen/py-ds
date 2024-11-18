import numpy as np

data = np.arange(9).reshape([3,3])

# Calculate the sum over the entire array.
print('Sum of whole array:', np.sum(data))

# Collapse axis 0 (i.e. collapse the rows), to get sum on each column.
print('Sum for each column:', np.sum(data, axis=0))

# Collapse axis 1 (i.e. collapse the columns), to get sum on each row.
print('Sum for each row:', np.sum(data, axis=1))