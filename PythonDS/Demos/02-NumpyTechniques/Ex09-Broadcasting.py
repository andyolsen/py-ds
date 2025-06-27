import numpy as np

a = np.array([10, 11, 12])
print(a.shape)       # (3,)

m = np.array([[20, 21, 22], [30, 31, 32]])
print(m.shape)       # (2,3)

result = a + m       
print(result.shape)  # (2, 3)
print(result)        # [[30 32 34] [40 42 44]]