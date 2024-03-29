import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import emcee
import corner

# Funzione che approssima andameto dati csv
def func(p, E):
    m, b, alpha, mu, sigma = p
    return ((m*E)+b+(alpha*np.exp(-((E-mu)**2)/(2*sigma**2) ) ))

# Probabilità logaritmiche
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

# Funzioni di proposta e valutazione passi del metodo Metropolis-Hastings
def mhprop(nparams):
    return np.random.uniform(-0.01, 0.01, size=nparams)

def mheval(pnow, pnext, fpb, data):
    energy, flow, ferr = data
    fpbnow = fpb(pnow, energy, flow, ferr)
    fpbnext = fpb(pnext, energy, flow, ferr)
    if fpbnext >= fpbnow:
        return fpbnext
    else:
        if np.random.random() < fpbnext/fpbnow : #np.exp(fpbnext-fpbnow)
            return pnext
        else:
            return pnow

        
### Tab
#tab = pd.read_csv('/home/lm010009/Scrivania/get-mcf-data/get_data.py/absorption_line.csv')
tab = pd.read_csv('absorption_line.csv')
print(tab)

energy = tab['E'].values
flow = tab['f'].values
ferr = tab['ferr'].values



### Manual mcmc
p0 = np.array([-1, 1, -1.0, 3, 0.1])
nparams  = len(p0)
#########################################################problemi
mychain = np.empty((3000,len(p0)))
#mychain = np.array([p0])
mychain = np.append(mychain, [p0], axis=0)
#print(mychain, mychain.shape)
for i in range(3000):
    proppos = mychain[-1]+mhprop(nparams)
    newpos = mheval(mychain[-1], proppos, lnprob_fl, (energy, flow, ferr))
    print(type(newpos), '\n', newpos)
    mychain = np.append(mychain, [newpos] , axis=0)

print('mychain:', mychain)
mychain = mychain.reshape(3001, 5)
print('mychainreshape:', mychain)

### Grafico walker per i parametri liberi
labels = ['m', 'b', r'$\alpha$', r'$\mu$', r'$\sigma$' ]

fig, axes = plt.subplots(nparams, figsize=(10, 9), sharex=True)
for i in range(nparams):
    axes[i].plot(mychain[:, i], color='darkred', alpha=0.3)
    axes[i].set_xlim(0, len(mychain))
    axes[i].set_ylabel(labels[i])
    #axes[i].yaxis.set_label_coords(-0.1, 0.5)

axes[-1].set_xlabel('numero passi')
plt.savefig('SamplerParamsMH.png')
plt.show()




### Confronto
# Grafico dati con alcuni campionamenti dei paramtri
plt.errorbar(energy, flow, yerr=ferr, fmt='o-', color='black', label='dati')
plt.xlabel('Energia')
plt.ylabel('Flusso')
# Ultimi 500 passi
select_chain = mychain[-500:-1]
print(mychain.shape, '\n', selecte_chain.shape)
# Grafico 50 campionamenti distribuzione a posteriori
en = np.arange(1, 10, 0.02)
for s in np.random.randint(len(select_chain), size=50):
    plt.plot(en, func(select_chain[s], en), color="green", alpha=0.3)
plt.legend()
plt.savefig('ConfrontoMH.png')
plt.show()




### Corner plot
struth = (-0.2, 10, -5, 4.8, 0.6)
fig = corner.corner( select_chain, labels=labels, truths=struth, show_titles=True, color='green')
plt.savefig('CornerMH.png')
plt.show()
