# Cálculo da rigidez à flexão dos pilares

import numpy as np
import pandas as pd

kp = np.zeros(4)
kn = np.zeros(4)
k = np.zeros(4)

# Constantes
Ec = 21e6  # kN/m2
Gn = 1000.0  # kN/m2
d = 1.0  # m
L = np.array([8.0, 10.0, 8.0, 5.0])  # m
hn = 0.024  # m
An = 0.21814  # m2

# Cálculos
Ip = np.pi * d**4 / 64.0
kp = 3.0 * Ec * Ip / L**3
kn = [Gn * An / hn, 0.00, 0.00, Gn * An / hn] # Pilares P2 e P3 sem aparelho de neoprene
deltap = 1.0 / kp
deltan = [hn / (Gn * An), 0.00, 0.00, hn / (Gn * An)] # Pilares P2 e P3 sem aparelho de neoprene
k = 1.0 / (deltan + deltap)

# Criação do DataFrame
datadict = {
    'pilar': ['P1', 'P2', 'P3', 'P4'],
    'altura': L,
    'rigidez_pilar': kp,
    'rigidez_neoprene': kn,
    'rigidez_total': k
}
data = pd.DataFrame(datadict)

# Imprimindo o DataFrame formatado
print("Tabela 5.6.2 - Rigidezes dos pilares da ponte")
print("Pilar    L(m)   kp(kN/m)     kn(kN/m)      k(kN/m)")
print("-" * 55)  # Linha separadora
print(data.to_string(index=False, header=False, float_format="{:10.2f}".format))