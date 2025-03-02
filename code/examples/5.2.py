from lib.ztransform import ZT, ztransform
from lib.inverse_ztransform import inverse_ztransform
import matplotlib.pyplot as plt
from sympy import KroneckerDelta
import sympy as sp
import numpy as np

# Definição das variáveis simbólicas
n, z, beta = sp.symbols('n z beta', integer=True)

# Determine as transformadas z de

#a) δ[n]
# Define o impulso unitário 
x_n = sp.KroneckerDelta(n, 0) 

# Calcula a Transformada Z
X_z = ztransform(x_n, n, z)
X_z = sp.simplify(X_z).doit()
print(X_z)


#b) u[n]
# Definindo o degrau
x_n = sp.Heaviside(n, 1) 

# Calcula a Transformada Z
X_z = ztransform(x_n, n, z)
print(X_z)

# c) cos(beta*n)u[n]
# Define o sinal x[n] = cos(beta * n) * u[n]
x_n = sp.cos(beta * n) * sp.Heaviside(n, 1)

# Calcula a Transformada Z 
X_z = ztransform(x_n, n, z)
print(X_z)

#d) Para o sinal do Gráfico

# Define o intervalo de n (de -2 a 10)
n_ = np.arange(-2, 11)  # Array NumPy

# Define o sinal x_n usando o array n_
x_n = np.where((n_ >= 0) & (n_ <= 4), 1, 0)  # Usar n_ (array) aqui!

# Plot do sinal
plt.stem(n_, x_n, basefmt=" ")
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Sinal x[n] = 1 para 0 <= n <= 4')
plt.grid(True)
plt.show()

# Define o sinal como soma de impulsos em n = 0,1,2,3,4
x_n = sum([KroneckerDelta(n, k) for k in range(0, 5)])

# Calcula a transformada
X_z = ztransform(x_n, n, z) 
X_z = sp.simplify(X_z)
print(X_z)