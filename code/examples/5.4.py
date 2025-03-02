import sympy as sp
from lib.ztransform import ZT, ztransform

# Definir as variáveis
z, n = sp.symbols('z n', real=True)

# Definir o sinal no domínio do tempo
x_n = n * (sp.Heaviside(n) - sp.Heaviside(n - 6))  # nu[n] - nu[n-6]

# Expressão rearranjada: x[n] = nu[n] - (n-6)u[n-6] - 6u[n-6]
x_n_rearranged = n * sp.Heaviside(n) - (n - 6) * sp.Heaviside(n - 6) - 6 * sp.Heaviside(n - 6)

# Calcular a Transformada Z
X_z = ztransform(x_n_rearranged, n, z)

# Exibir o resultado
X_z

print(X_z)
