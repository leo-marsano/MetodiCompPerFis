import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

tab = pd.read_csv('vel_vs_time.csv')

v = tab['v']
t = tab['t']

#print('distanza percorsa in funzione del tempo ', integrate.simpson(v,t))

x = np.zeros(len(t))
for i in range(0, len(t)):
    x[i] = integrate.simpson(v[:i+1],t[:i+1])

print(x[-1], '\n', integrate.simpson(v,t), '\n', x)


fig, ax = plt.subplots(1,2, figsize=(12,6))
ax[0].plot(t, v,color='darkviolet')
ax[1].plot(t, x,color='cyan')

ax[0].set_title('Velocita\'', fontsize=15, color='darkviolet')
ax[1].set_title('Distanza percorsa', fontsize=15, color='cyan')

ax[0].set_xlabel('tempo [s]')
ax[0].set_ylabel('velocita [m/s]')

ax[1].set_xlabel('tempo [s]')
ax[1].set_ylabel('spazio [m]')

ax[0].grid(True)
ax[1].grid(1)

plt.show()
