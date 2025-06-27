import numpy as np
from timeit import default_timer as timer

def compute_cubes_ufunc(data):
    result = data ** 3
    return result

np.random.seed(0)
data = np.random.randint(1, 10, size=10_000_000)

start = timer()
cubes = compute_cubes_ufunc(data)
end = timer()
print('Execution time using a ufunc', end - start)