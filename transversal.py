# Distribuição dos esforços transversais do vento nos pilares da ponte
import numpy as np
import pandas as pd
r = np.zeros(4)
fp_w_transv = np.zeros(4)
xg = np.zeros(4)
kx = np.zeros(4)
kx2 = np.zeros(4)

Hwt = 655.94 # kN
x=np.array([45.00, 25.00, 0.00, -20.00])
k = np.array([3628.68, 3092.51, 6040.05, 6647.11])
somak = sum(k)
r=k/somak

kx = np.dot(k,x)
kx2 = np.dot(kx,x)
xg0 = kx/sum(k)
xg = x - xg0
Ixg = sum(k*xg**2)
e = 12.50 - xg0
cd = k*(1.00/somak + e/Ixg*xg)
fp_w_transv = cd*Hwt

print(f'xg0 = {xg0:10.2f} m')
print(f'Ixg = {Ixg:10.2f} kNm')
print(f'e = {e:10.2f} m')
print()

print('Tabela 5.6.5 - Forças longitudinais nos pilares devidas ação do vento')
print('Pilar      k(kN/m)        cd        Força (kN)')
                      
datadict2 = {'pilar': ['P1','P2','P3','P4'], 'rigidez': k, 'coef_dist': cd, 'forca_vento_transv': fp_w_transv}
data2 = pd.DataFrame(datadict2)

# Imprimindo o DataFrame sem nomes de colunas e índices de linhas, com formatação
formatted_data = data2.copy()  # Criamos uma cópia para não modificar o DataFrame original
formatted_data['rigidez'] = formatted_data['rigidez'].apply(lambda x: "{:15.2f}".format(x))
formatted_data['coef_dist'] = formatted_data['coef_dist'].apply(lambda x: "{:10.4f}".format(x))
formatted_data['forca_vento_transv'] = formatted_data['forca_vento_transv'].apply(lambda x: "{:15.2f}".format(x))

print(formatted_data.to_string(index=False, header=False))
print(f'Total  =           {sum(r):10.4f}      {sum(fp_w_transv):10.2f}')
