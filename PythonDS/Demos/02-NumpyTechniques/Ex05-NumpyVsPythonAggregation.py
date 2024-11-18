import numpy as np
from timeit import default_timer as timer

data = np.random.rand(100_000_000)

start1 = timer()
result1 = sum(data)      # Python sum() function
end1 = timer()
print('Execution time using Python sum():  ', end1 - start1)

start2 = timer()
result2 = np.sum(data)   # NumPy sum() function
end2 = timer()
print('Execution time using NumPy sum(): ', end2 - start2)