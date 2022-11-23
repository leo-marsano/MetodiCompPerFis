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


Nsteps = np.array([10, 100, 1000])
Nrw = 100
rwstep = 1

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
