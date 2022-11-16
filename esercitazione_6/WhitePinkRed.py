import numpy as np
import pandas as pd
from scipy import constants, fft
import matplotlib.pyplot as plt
import scipy.optimize as opt

def fbeta(f, b, A):
    return A/(f)**b


#tabs
tab1 = pd.read_csv('/home/lm010009/Scrivania/get-mcf-data/get_data.py/data_sample1.csv')
print(tab1)

tab2 = pd.read_csv('/home/lm010009/Scrivania/get-mcf-data/get_data.py/data_sample2.csv')
print(tab2)

tab3 = pd.read_csv('/home/lm010009/Scrivania/get-mcf-data/get_data.py/data_sample3.csv')
print(tab3)

#ft
time = tab1['time']
noise1 = tab1['meas'].values
noise2 = tab2['meas'].values
noise3 = tab3['meas'].values

ftnoise1 = fft.rfft(noise1)
ftnoise2 = fft.rfft(noise2)
ftnoise3 = fft.rfft(noise3)
dt = 1
nq = 0.5
ftnoise1f = nq*fft.rfftfreq(ftnoise1.size, dt)
ftnoise2f = nq*fft.rfftfreq(ftnoise2.size, dt)
ftnoise3f = nq*fft.rfftfreq(ftnoise3.size, dt)

#noiseplot
'''
plt.plot(time, noise1, label='white noise')
plt.plot(time, noise2, label='pink noise')
plt.plot(time, noise3, label='red noise')
plt.xlabel('tempi')
plt.ylabel('noise')
plt.legend()
plt.show()
'''

#noisecoeff
'''
plt.plot(np.absolute(ftnoise1[:len(ftnoise1)//2])**2, 'o', markersize=4, label='white')
plt.plot(np.absolute(ftnoise2[:len(ftnoise2)//2])**2, 'o', markersize=4, label='pink')
plt.plot(np.absolute(ftnoise3[:len(ftnoise3)//2])**2, 'o', markersize=4, label='red')

plt.xlabel('Indice')
plt.ylabel('$|c_k|^2$')
plt.xscale('log')
plt.yscale('log')

plt.legend()
plt.show()
#plt.savefig('coefficienti.pdf')
'''

#noisefit
pstart = np.array([0, 1])
params1, params1_covariance = opt.curve_fit(fbeta, ftnoise1f[1:ftnoise1.size//2], np.absolute(ftnoise1[1:ftnoise1.size//2])**2, p0=[pstart])
ftnoisefit1 = fbeta(ftnoise1f[1:ftnoise1.size//2], params1[0], params1[1])
params2, params2_covariance = opt.curve_fit(fbeta, ftnoise2f[1:ftnoise2.size//2], np.absolute(ftnoise2[1:ftnoise2.size//2])**2, p0=[pstart])
ftnoisefit2 = fbeta(ftnoise2f[1:ftnoise2.size//2], params2[0], params2[1])
params3, params3_covariance = opt.curve_fit(fbeta, ftnoise3f[5:ftnoise3.size//2], np.absolute(ftnoise3[5:ftnoise3.size//2])**2, p0=[pstart])
ftnoisefit3 = fbeta(ftnoise3f[5:ftnoise3.size//2], params3[0], params3[1])
print(params1, '\n', params2, '\n', params3, '\n') 

plt.plot(ftnoise1f[:int(ftnoise1.size/2)], np.absolute(ftnoise1[:int(ftnoise1.size/2)])**2, 'o', markersize=4, label='white', color='blue')
plt.plot(ftnoise2f[:int(ftnoise2.size/2)], np.absolute(ftnoise2[:int(ftnoise2.size/2)])**2, 'o', markersize=4, label='pink', color='violet')
plt.plot(ftnoise3f[:int(ftnoise3.size/2)], np.absolute(ftnoise3[:int(ftnoise3.size/2)])**2, 'o', markersize=4, label='red', color='red')
plt.plot(ftnoise1f[1:ftnoise1.size//2], ftnoisefit1, '-', label='white fit', color='darkblue')
plt.plot(ftnoise2f[1:ftnoise2.size//2], ftnoisefit2, '-', label='pink fit', color='darkviolet')
plt.plot(ftnoise3f[5:ftnoise3.size//2], ftnoisefit3, '-', label='red fit', color='darkred')

plt.xlabel('Frequenza [1/yr]')
plt.ylabel('$|c_k|^2$')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
