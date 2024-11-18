import numpy as np

a = np.arange(10)

print('Using operators')
print('a + 2  = ', a + 2)
print('a - 2  = ', a - 2)
print('a * 2  = ', a * 2)
print('a / 2  = ', a / 2)
print('a // 2 = ', a // 2)
print('a % 2  = ', a % 2)
print('a ** 2 = ', a ** 2)

print('\nUsing ufuncs explicitly')
print('np.add(a, 2)          = ', np.add(a, 2))
print('np.subtract(a, 2)     = ', np.subtract(a, 2))
print('np.multiply(a, 2)     = ', np.multiply(a, 2))
print('np.divide(a, 2)       = ', np.divide(a, 2))
print('np.floor_divide(a, 2) = ', np.floor_divide(a, 2))
print('np.mod(a, 2)          = ', np.mod(a, 2))
print('np.power(a, 2)        = ', np.power(a, 2))