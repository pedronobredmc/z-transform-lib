from lib.ztransform import ZT, ztransform
from lib.inverse_ztransform import inverse_ztransform
from sympy import symbols, apart, Eq, Heaviside, Rational
from sympy import simplify, expand, factor, solve, denom, numer, Pow, Function
import sympy as sp

# Determinar a tranformada z de 
#               X[z] = -z(z+0.4)/(z-0.8)(z-2)

z = sp.symbols('z', real=True)
n = sp.symbols('n', Interge=True)

#decomposição em frações parciais
x_z = (-z*(z+0.4))/((z-0.8)*(z-2))
expr = x_z/z
x_zpartial = apart(expr)
x_zpartial = z * x_zpartial

#a) para RDC |z| > 2
#como a RDC é |z| > 2, os dois termos correspondem a sequências causais
x_a = inverse_ztransform(x_zpartial, z, n, 
                               causal=True)
print(x_a)

#b)para RDC |z| < 0.8
#Neste caso, |z| < 0,8, o que é menor do que as magnitudes dos dois polos. 
#Logo, os dois termos cor-respondem a sequências anticausais.
x_b = inverse_ztransform(x_zpartial, z, n, 
                               causal=False)
print(x_b)

#c) para RDC 0.8 < |z| < 2
#Neste caso, 0,8 < |z| < 2, a parte de X[z] que corresponde ao polo em 0,8 é uma sequência causal 
# e a parte correspondente ao polo 2 é uma sequência anticausal.

term1 = z/(z-0.8)
term2 = -2*z/(z-2)

x_c1 = inverse_ztransform(term1, z, n, 
                               causal=True)
x_c2 = inverse_ztransform(term2, z, n, 
                               causal=False)
x_c = x_c1+x_c2

print(x_c)