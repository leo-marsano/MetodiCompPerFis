import sys
import numpy as np
import matplotlib.pyplot as plt
import math

def random_walk2Dasimm(step, phi):
    deltax=np.zeros(len(phi)+1)
    deltay=np.zeros(len(phi)+1)
    spostx = 0
    sposty = 0
    for r in range(len(phi)):
        spostx = spostx + step*np.cos(phi[r])
        sposty = sposty + step*np.sin(phi[r])
        deltax[r+1] = spostx
        deltay[r+1] = sposty
    return deltax, deltay

def invcum(y):
    return 2*np.arccos(1-2*y)


### Hist
nsample = 10000
ycum = np.random.random(nsample)
xicum = invcum(ycum)

fig, ax = plt.subplots(1,2, figsize=(11,5))
ax[0].hist(ycum, bins=100, range=(0,1), color='cyan',   ec='darkcyan')
ax[0].set_title('Distribuzione y Cumulativa')
ax[0].set_xlabel('y cumulativa')

ax[1].hist(xicum, bins=100, range=(0,2*math.pi), color='orange', ec='darkorange')
ax[1].set_title(r'Distribuzione secondo la funzione $p(\phi)= \frac{1}{4}sin(\frac{\phi}{2})$')
ax[1].set_xlabel('x')
plt.savefig('hist_asim.png')
plt.show()

### 5 Random walk
Nsteps = np.array([10, 100, 1000])
Nrw = 5
rwstep = 1

for i in range(Nrw):
    ycum = np.random.random(nsample)
    xicum = invcum(ycum)
    x, y = random_walk2Dasimm(rwstep, xicum)
    plt.plot(x, y,label='random walk {:}'.format(i+1))
 
plt.plot(0, 0, 'ro', linewidth=10, color='black', label='starting point')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title(r'5 random walk con probabilita\' asimmetrica di $\phi$ : $p(\phi)= \frac{1}{4}sin(\frac{\phi}{2})$')
plt.savefig('5rw_asim.png')
plt.show()

### 100 Random walk
for i in range(Nrw):
    x, y = random_walk2Dsimm(rwstep, Nsteps[2])
    plt.plot(x[Nsteps[2]], y[Nsteps[2]], 'ro', color = 'lightgreen',label='random walk {:}'.format(i+1))
    plt.plot(x[Nsteps[1]+1], y[Nsteps[1]+1], 'ro', color = 'purple',label='random walk {:}'.format(i+1))
    plt.plot(x[Nsteps[0]+1], y[Nsteps[0]+1], 'ro', color = 'darkorange', label='random walk {:}'.format(i+1))

    
plt.plot(0, 0, 'ro', linewidth=10, color='black', label='starting point')
plt.xlabel('x')
plt.ylabel('y')
#plt.legend()
plt.savefig('1000rw.png')
plt.show()






