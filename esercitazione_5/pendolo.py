from scipy import integrate, constants
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def pendulum(thetav, t, l):
    """
    thetav : vettore con variabili (theta,dtheta/dt)
    t  : variabile tempo
    l : lunghezza del pendolo semplice
    
    g = 9.80314 m/s^2 : costante gravitazionale a Perugia
    """
    g = constants.g
    dthetadt = thetav[1]
    domegadt = - g*np.sin(thetav[0])/l
    
    return (dthetadt, domegadt)

#time array
dt = 0.01 #s
tt = np.arange(0, 10, dt)

#initial conditions
l1 = 1 #m
theta01 = np.radians(45) #°
#theta01 = np.radians(45) #rad
l2 = 0.5 #m
#theta02 = 30 #°
theta02 = np.radians(30) #°
omega0 = 0 #rad/s

icond1 = (theta01, omega0)
icond2 = (theta02, omega0)

#solutions
sol1 = integrate.odeint(pendulum, icond1, tt, args=(l1,))
sol2 = integrate.odeint(pendulum, icond1, tt, args=(l2,))
sol3 = integrate.odeint(pendulum, icond2, tt, args=(l2,))

#grafico soluzioni
plt.figure(figsize=(10, 4))
plt.plot(tt, np.degrees(sol1[:,0]), color='olivedrab', label=r'$\theta_0 = 45°; l = 1m$')
plt.plot(tt, np.degrees(sol2[:,0]), color='orange', label=r'${\theta}_0$ = 45°; l = 0.5m')
plt.plot(tt, np.degrees(sol3[:,0]), color='maroon', label=r'${\theta}_0$ = 30°; l = 0,5m')
plt.title('soluzione equazione diff. pendolo semplice con diverse c. iniziali')
plt.xlabel('time [s]')
plt.ylabel(r'$\theta$ [deg]')
plt.legend(loc='upper right')
#plt.savefig('pendulum.png')
plt.show()
