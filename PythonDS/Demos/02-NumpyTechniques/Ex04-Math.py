import numpy as np
import scipy.special as sp

a = np.linspace(0, np.pi, 3)
print('sin(a)  = ', np.sin(a))
print('cos(a)  = ', np.cos(a))
print('tan(a)  = ', np.tan(a))
print('sinh(a) = ', np.sinh(a))
print('cosh(a) = ', np.cosh(a))
print('tanh(a) = ', np.tanh(a))

b = np.linspace(0.1, 0.9, 3)
print('arcsin(b)  = ', np.arcsin(b))
print('arccos(b)  = ', np.arccos(b))
print('arctan(b)  = ', np.arctan(b))
print('arcsinh(b) = ', np.arcsinh(b))
print('arccosh(b) = ', np.arccosh(b))
print('arctanh(b) = ', np.arctanh(b))

c = np.array([1, 10, 100])
print('log(c)   = ', np.log(c))
print('log2(c)  = ', np.log2(c))
print('log10(c) = ', np.log10(c))
print('exp(c)   = ', np.exp(c))
print('exp2(c)  = ', np.exp2(c))
print('exp10(c) = ', sp.exp10(c))