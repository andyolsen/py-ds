import numpy as np
from timeit import default_timer as timer

def compute_cubes_loop(data):
    result = np.empty(len(data))
    for i in range(len(data)):
        result[i] = data[i] ** 3    
    return result

np.random.seed(0)
data = np.random.randint(1, 10, size=10_000_000)

start = timer()
cubes = compute_cubes_loop(data)
end = timer()
print('Execution time using a loop', end - start)