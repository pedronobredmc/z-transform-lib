import sympy as sp
from lib.ztransform import ZT

# Definição das variáveis
z, n = sp.symbols('z n', real=True)

# Expressões dos resultados nas equações 5.84 e 5.85
X1_z = z / (z - 0.9)  # Para |z| > 0.9
X2_z = -z / (z - 1.2)  # Para |z| < 1.2

# Soma das transformadas Z
X_z = X1_z + X2_z

# Simplificação da expressão final
X_z_simplified = sp.simplify(X_z)

# Exibir a Transformada Z final
X_z_simplified

print(X_z_simplified)
