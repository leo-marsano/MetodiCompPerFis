import numpy as np
from scipy.optimize import minimize
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import emcee
import corner
import time

def func(p, E):
    m, b, alpha, mu, sigma = p
    return ((m*E)+b+(alpha*np.exp(-((E-mu)**2)/(2*sigma**2) ) ))

def lnlike_fl(p, energy, flow, ferr):
    return -0.5 * np.sum(((flow - func(p, energy))/ferr) ** 2)

def lnprior_fl(p):
    m, b, alpha, mu, sigma = p
    if ( -1 < m < 0 and  5 < b < 15 and  -10 < alpha < 0 and  0 < mu < 10
         and  0 < sigma < 3):
        return 0.0
    return -np.inf

def lnprob_fl(p, energy, flow, ferr):
    lp = lnprior_fl(p)
    
    if np.isfinite(lp):
        return lp + lnlike_fl(p, energy, flow, ferr) 
    
    return -np.inf



### Tab
#tab = pd.read_csv('/home/lm010009/Scrivania/get-mcf-data/get_data.py/absorption_line.csv')
tab = pd.read_csv('absorption_line.csv')
print(tab)

energy = tab['E'].values
flow = tab['f'].values
ferr = tab['ferr'].values

plt.errorbar(energy, flow, yerr=ferr, color='salmon')
#plt.legend(fontsize=13)
plt.xlabel('Energia')
plt.ylabel('Flusso')
plt.title('dati csv', fontsize = 12)
#plt.xscale('log')
#plt.yscale('log')
#plt.savefig('daticsv.png')
#plt.show()




### Stimo
params=(-0.18, 10, -5, 5, 0.8)
plt.errorbar(energy, flow, yerr=ferr, color='salmon', label='dati')
plt.plot(energy, func(params, energy), color='cyan', label='funzione')
plt.legend()
plt.xlabel('Energia')
plt.ylabel('Flusso')
plt.title('dati csv')
plt.savefig('daticsv.png')
plt.show()




### Emcee sampler
# numero walker
nw = 32
# condizioni iniziali
initial_fl = params
ndim_fl = len(initial_fl)
p0 = np.array(initial_fl)  +0.1*np.random.randn(nw, ndim_fl)
# definisco il sampler di emcee
sampler_fl = emcee.EnsembleSampler(nw, ndim_fl, lnprob_fl, args=(energy, flow, ferr))
# Lancio campionamento per 3000 passi
print("Running production...")
sampler_fl.run_mcmc(p0, 3000, progress=True); #per evitare print

# Grafico walker per i parametri liberi
fig, axes = plt.subplots(ndim_fl, figsize=(10, 9), sharex=True)
samples_fl = sampler_fl.get_chain()

labels = ['m', 'b', r'$\alpha$', r'$\mu$', r'$\sigma$' ]
for i in range(ndim_fl):
    ax = axes[i]
    ax.plot(samples_fl[:, :, i], color='darkblue', alpha=0.3)
    ax.set_xlim(0, len(samples_fl))
    ax.set_ylabel(labels[i])
    #ax.yaxis.set_label_coords(-0.1, 0.5)

axes[-1].set_xlabel('numero passi')
plt.savefig('SamplerParams.png')
plt.show()




### Confronto
# Grafico dati con alcuni campionamenti dei paramtri
plt.errorbar(energy, flow, yerr=ferr, fmt='o-', color='black', label='dati')
plt.xlabel('Energia')
plt.ylabel('Flusso')
# Escludo i primi 300 passi dalla valutazione 
flat_samples_fl = sampler_fl.get_chain(discard=300, thin=40, flat=True)
print(samples_fl.shape)
# Grafico 40 campionamenti distribuzione a posteriori
samples_fl = sampler_fl.flatchain
for s in samples_fl[np.random.randint(len(samples_fl), size=15)]:
    plt.plot(energy, func(s, energy), color="orange", alpha=0.3)
plt.legend()
plt.savefig('Confronto.png')
plt.show()




### Corner plot
#struth = (-0.21, 10.05, -5, 4.83, 0.6)
fig = corner.corner( flat_samples_fl, labels=labels, show_titles=True, color='orange')
plt.savefig('Corner.png')
plt.show()
