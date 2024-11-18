import numpy as np

b = np.array([[0, 10, 20], [30, 40, 50], [60, 70, 80]])
col0Copy = b[:, 0].copy()
col0Copy[2] = 600
print(col0Copy)
print(b)   # [[ 0  10  20] [ 30  40  50] [60  70  80]]