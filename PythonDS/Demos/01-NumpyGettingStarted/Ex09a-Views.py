import numpy as np

a = np.array([[0, 10, 20], [30, 40, 50], [60, 70, 80]])
col0View = a[:, 0]
col0View[2] = 600
print(col0View)
print(a)   # [[ 0  10  20] [ 30  40  50] [600  70  80]]