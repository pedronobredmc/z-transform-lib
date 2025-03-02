from lib.ztransform import ZT, ztransform
from lib.inverse_ztransform import inverse_ztransform
import sympy as sp

z = sp.symbols('z', real=True)
n = sp.symbols('n', real=True)

x = n**2*sp.Heaviside(n)

print(ZT(x, n, z))

x_z = z / (z-1)**2
print(inverse_ztransform(x_z, z, n))