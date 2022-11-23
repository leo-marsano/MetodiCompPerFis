import numpy as np
import matplotlib.pyplot as plt
import math

def random_walk2Dsimm(step, N):
    deltax=np.zeros(N+1)
    deltay=np.zeros(N+1)
    spostx = 0
    sposty = 0
    phi = 2*math.pi*np.random.random(N)
    for r in range(len(phi)):
        spostx = spostx + step*np.cos(phi[r])
        sposty = sposty + step*np.sin(phi[r])
        deltax[r+1] = spostx
        deltay[r+1] = sposty
    return deltax, deltay

### 5 Random walk
Nsteps = np.array([10, 100, 1000])
Nrw = 5
rwstep = 1

for i in range(Nrw):
    x, y = random_walk2Dsimm(rwstep, Nsteps[2])
    plt.plot(x, y,label='random walk {:}'.format(i+1))
 
plt.plot(0, 0, "ro", linewidth=10, color='black', label='starting point')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title(r'5 random walker con probabilità simmetrica per $\phi$')
plt.savefig('5rw.png')
plt.show()

### 1000 Random walk
Nrw = 1000
xx = np.empty((0,3))
yy = np.empty((0,3))

distquad=np.empty((0, Nsteps[2]+1))
distquad2=np.empty((0, Nsteps[2]+1))

for i in range(Nrw):
    x, y = random_walk2Dsimm(rwstep, Nsteps[2])
    x2, y2 = random_walk2Dsimm(2*rwstep, Nsteps[2])
    distquad = np.append(distquad, np.sum([x*x, y*y], axis=0))
    distquad2 = np.append(distquad2, np.sum([x2*x2, y2*y2], axis=0))
    xx = np.append(xx, np.array([[ x[Nsteps[0]],  x[Nsteps[1]], x[Nsteps[2]] ]]), axis=0)
    yy = np.append(yy, np.array([[ y[Nsteps[0]],  y[Nsteps[1]], y[Nsteps[2]] ]]), axis=0)

plt.plot(xx[:,2], yy[:,2], 'o', color='darkorange', label='dopo 1000 passi')
plt.plot(xx[:,1], yy[:,1], 'o', color='purple', label='dopo 100 passi')
plt.plot(xx[:,0], yy[:,0], 'o', color='lightgreen', label='dopo 10 passi')
plt.plot(0, 0, 'ro', linewidth=10, color='black', label='starting point')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title(r'posizione di 1000 random walker con probabilità simmetrica per $\phi$')
plt.savefig('1000rw.png')
plt.show()


### Distanza quadratica media
plt.plot(np.mean((distquad.reshape(1000, 1001))**0.5, axis=0), '-', label='passo1')
plt.plot(np.mean((distquad2.reshape(1000, 1001))**0.5, axis=0), '-', label='passo2')
plt.ylabel(r'$ \Delta \bar x$')
plt.xlabel('numero passi')
plt.legend()
plt.title('distanza quadratica media per la diffuzione simmetrica')
plt.savefig('distquadmed.png')
plt.show()
