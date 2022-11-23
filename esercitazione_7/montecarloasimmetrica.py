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
 
plt.plot(0, 0, "ro", linewidth=10, color='black', label='starting point')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title(r'5 random walker con probabilità asimmetrica di $\phi$ : $p(\phi)= \frac{1}{4}sin(\frac{\phi}{2})$')
plt.savefig('5rw_asim.png')
plt.show()

### 1000 Random walk
Nrw = 1000
xx = np.empty((0,3))
yy = np.empty((0,3))

for i in range(Nrw):
    ycum = np.random.random(nsample)
    xicum = invcum(ycum)
    x, y = random_walk2Dasimm(rwstep, xicum)
    xx = np.append(xx, np.array([[ x[Nsteps[0]],  x[Nsteps[1]], x[Nsteps[2]] ]]), axis=0)
    yy = np.append(yy, np.array([[ y[Nsteps[0]],  y[Nsteps[1]], y[Nsteps[2]] ]]), axis=0)

plt.plot(xx[:,0], yy[:,0], 'o', color='lightgreen', label='dopo 10 passi')
plt.plot(xx[:,1], yy[:,1], 'o', color='purple', label='dopo 100 passi')
plt.plot(xx[:,2], yy[:,2], 'o', color='darkorange', label='dopo 1000 passi')
plt.plot(0, 0, 'ro', linewidth=10, color='black', label='starting point')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title(r'posizione di 1000 random walker con probabilità asimmetrica di $\phi$ : $p(\phi)= \frac{1}{4}sin(\frac{\phi}{2})$')
plt.savefig('1000rw_asim.png')
plt.show()






