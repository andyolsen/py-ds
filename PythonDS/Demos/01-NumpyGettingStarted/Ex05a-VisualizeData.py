import numpy as np
import matplotlib.pyplot as plt

data = np.array([1, 19, 76, 45, 34, 42, 30, 5, 77, 54, 89])

plt.xlabel('Element in array')
plt.ylabel('Value')
plt.plot(data)

plt.show()