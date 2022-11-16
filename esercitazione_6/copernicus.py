import numpy as np
import pandas as pd
from scipy import constants, fft
import matplotlib.pyplot as plt
import scipy.optimize as opt

### Tab
tab = pd.read_csv('/home/lm010009/Scrivania/get-mcf-data/get_data.py/copernicus_PG_selected.csv')
#tab = pd.read_csv('copernicus_PG_selected.csv')
#print(tab)

time = (tab['date'].values)-58112.0
co = tab['mean_co_ug/m3'].values
cok = tab['mean_co_ug/m3']
nh3 = tab['mean_nh3_ug/m3'].values
no2 = tab['mean_no2_ug/m3'].values
o3 = tab['mean_o3_ug/m3'].values
pm10 = tab['mean_pm10_ug/m3'].values
pm2p5 = tab['mean_pm2p5_ug/m3'].values
so2 = tab['mean_so2_ug/m3'].values

### Inquinanti

fig,ax = plt.subplots(7,1, figsize = (40,40))

ax[0].plot(time, co, '-', color = 'rebeccapurple')
ax[1].plot(time, nh3, '-', color = 'goldenrod')
ax[2].plot(time, no2, '-', color = 'limegreen')
ax[3].plot(time, o3, '-', color = 'violet')
ax[4].plot(time, pm10, '-', color = 'salmon')
ax[5].plot(time, pm2p5, '-', color = 'olive')
ax[6].plot(time, so2, '-', color = 'dodgerblue')

ax[0].set_title('monossido di carbonio', loc='left', y=0.75, x=0.02)
ax[1].set_title('ammonio', loc='left', y=0.75, x=0.02)
ax[2].set_title('biossido di azoto', loc='left', y=0.75, x=0.02)
ax[3].set_title('ozono', loc='left', y=0.75, x=0.02)
ax[4].set_title('pm10', loc='left', y=0.75, x=0.02)
ax[5].set_title('pm2p5', loc='left', y=0.75, x=0.02)
ax[6].set_title('anidride solforosa', loc='left', y=0.75, x=0.02)

fig.suptitle('media della densità di INQUINANTI ATMOSFERICI [ug/m3] al variare dei giorni di campionamento', fontsize = 18)

plt.savefig('inquinanti.png')
plt.show()

### CO
ftco = fft.rfft(co)
dt = 1
nq = 0.5
ftcof = nq*fft.rfftfreq(ftco.size, dt)

figg,axx = plt.subplots(1, 2, figsize = (10,5))

axx[0].plot(ftcof[:len(ftco)//2], np.absolute(ftco[:len(ftco)//2])**2, 'o', markersize=4, label='spettro($\\nu$)')

# Periodicità
listmax = list(np.absolute(ftco[:len(ftco)//2]))
index = listmax.index(max(listmax))
listmax1 = list(np.absolute(ftco[1:len(ftco)//2]))
index1 = listmax.index(max(listmax1))
axx[0].axvline(ftcof[index],   color='red', label='1° freq')
axx[0].axvline(ftcof[index1],   color='orange', label='2° freq')

axx[0].set_xlabel('Frequenza [1/yr]')
axx[0].set_ylabel('$|c_k|^2$')
#axx[0].set_xscale('log')
axx[0].set_yscale('log')
axx[0].legend(loc=9) #'upper centre'

#inserzione
ins = axx[0].inset_axes([0.64, 0.58, 0.3,0.36])
ins.axvline(ftcof[index],   color='red', linewidth=2)
ins.axvline(ftcof[index1],   color='orange', linewidth=2)
ins.plot(ftcof[:len(ftco)//2], np.absolute(ftco[:len(ftco)//2])**2, 'o', markersize=4)
ins.set_xlim(-0.005,0.005)
ins.set_yscale('log')

axx[1].plot(1/ftcof[1:len(ftco)//2], np.absolute(ftco[1:len(ftco)//2])**2, 'o', markersize=4)
axx[1].set_xlabel('Periodo [yr]')
axx[1].set_ylabel(r'$|c_k|^2$')
axx[1].set_xscale('log')
axx[1].set_yscale('log')

figg.suptitle('spettro di potenza in funzione di frequenza $\\nu$ e periodo $T$', fontsize = 15)
plt.savefig('spettri.png')
plt.show()


### Mask
ftmask1 = np.absolute(ftco)**2< 5e7
ftmask2 = np.absolute(ftco)**2< 7e6

filtered_ftco1 = ftco.copy()
filtered_ftco1[ftmask1] = 0
filtered_ftco2 = ftco.copy()
filtered_ftco2[ftmask2] = 0
# Trasformata FFT inversa con coeff filtrati 
filtered_co1 = fft.irfft(filtered_ftco1, n=len(tab['mean_co_ug/m3']))
filtered_co2 = fft.irfft(filtered_ftco2, n=len(tab['mean_co_ug/m3']))

plt.subplots(figsize=(11,7))
plt.plot(time, tab['mean_co_ug/m3'], color='lightsalmon',      label='Dati Originali')
plt.plot(time, filtered_co2,     color='aqua', label='Filtro $coeff>7\cdot 10^6$')
plt.plot(time, filtered_co1,     color='darkviolet',   label='Filtro $coeff>5\cdot 10^7$')
plt.legend(fontsize=13)
plt.xlabel('Giorni')
plt.ylabel('Densità CO nell\'aria [ug/m3]')
plt.title('Segnali originale e filtrati sulla densità di CO', fontsize = 12)
plt.savefig('filtri.png')
plt.show()
