# Cálculo da rigidez à flexão dos pilares

import numpy as np
import pandas as pd

k = np.zeros(4)
kp = np.zeros(4)
kn = np.zeros(4)
deltap = np.zeros(4)
deltan = np.zeros(4)

Ec = 21.e6 # kN/m2
Gn = 1000. # kN/m2
d = 1.00 # m
L = np.array([8.00, 10.00, 8.00, 5.00]) # m
hn = 0.024 # m
An = 0.21814 # m2

Ip = np.pi*d**4/64.
kp = 3. * Ec * Ip /L**3
deltap = 1./kp
kn[0] = Gn*An / hn
kn[3] = kn[0]
deltan[0] = 1./ kn[0]
deltan[3] = 1./ kn[3]
k = 1./(deltan+deltap)

print('Pilar    L(m)   kp(kN/m)   kn(kN/m)    k(kN/m) ')
                      
datadict = {'pilar': ['P1','P2','P3','P4'], 'altura': L, 'rig_pilar': kp, 'rig_neoprene': kn,'rigidez': k}
data = pd.DataFrame(datadict)

# Imprimindo o DataFrame sem nomes de colunas e índices de linhas, com formatação
formatted_data = data.copy()  # Criamos uma cópia para não modificar o DataFrame original
formatted_data['altura'] = formatted_data['altura'].apply(lambda x: "{:10.2f}".format(x))
formatted_data['rig_pilar'] = formatted_data['rig_pilar'].apply(lambda x: "{:10.2f}".format(x))
formatted_data['rig_neoprene'] = formatted_data['rig_neoprene'].apply(lambda x: "{:10.2f}".format(x))
formatted_data['rigidez'] = formatted_data['rigidez'].apply(lambda x: "{:10.2f}".format(x))

print(formatted_data.to_string(index=False, header=False))

