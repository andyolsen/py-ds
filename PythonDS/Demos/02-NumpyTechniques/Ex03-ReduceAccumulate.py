import numpy as np

a = np.arange(2, 5)

print('reduce() examples')
print('Sum    ', np.add.reduce(a))
print('Product', np.multiply.reduce(a))
print('Power  ', np.power.reduce(a))

print('accumulate() examples')
print('Sum    ', np.add.accumulate(a))
print('Product', np.multiply.accumulate(a))
print('Power  ', np.power.accumulate(a))