import numpy as np

# Split a 1D array.
a = np.arange(16)
a1, a2, a3, a4 = np.split(a, [2, 5, 9])
print('\na1\n', a1)   # [0 1] 
print('\na2\n', a2)   # [2 3 4] 
print('\na3\n', a3)   # [5 6 7 8]
print('\na4\n', a4)   # [9 10 11 12 13 14 15]

# Split a 2D vertically.
b = np.arange(16).reshape((4, 4))
b1, b2 = np.vsplit(b, [3])
print('\ntop\n', b1)     # [[0 1 2 3] [4 5 6 7] [8 9 10 11]] 
print('\nbottom\n', b2)  # [[12 13 14 15]]

# Split a 2D horizontally.
c = np.arange(16).reshape((4, 4))
c1, c2 = np.hsplit(c, [3])
print('\nleft\n', c1)    # [[0 1 2] [4 5 6] [8 9 10] [12 13 14]] 
print('\nright\n', c2)   # [[3] [7] [11] [15]]