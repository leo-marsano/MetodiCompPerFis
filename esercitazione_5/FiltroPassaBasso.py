import scipy.integrate as intg
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def ode(vout, t, rc):
    #rc=np.array([1, 0.1, 0.01])
    vin = (int(t+1)%2)*2 -1
    return (vin-vout)/(rc) 

a=0
b=10
v0=0
n=10000
tt =np.arange(a, b, (b-a)/n)
RC=np.array([1, 0.1, 0.01])

vin = ((tt.astype(int)+1)%2)*2 -1
vv0 = intg.odeint(ode, v0, tt, args=((RC[0],)))
vv1 = intg.odeint(ode, v0, tt, args=((RC[1],)))
vv2 = intg.odeint(ode, v0, tt, args=((RC[2],)))


#plot
fig,ax = plt.subplots(figsize=(10,5))
plt.title('filtro passa basso', color='black', fontsize=14)

plt.plot(tt, vin, label='$V_{in}$')
plt.plot(tt, vv0, label='$V_{out} con RC=1$')
plt.plot(tt, vv1, label='$V_{out} con RC=0,1$')
plt.plot(tt, vv2, label='$V_{out} con RC=0,01$')

plt.xlabel('t [s]')
plt.ylabel('Volt [V]')
plt.legend(loc='lower right', fontsize=7)
plt.text(tt[0]-0.4, min(vv1),
         r'$\frac{dV_out}{dt} = \frac{1}{RC} (V_{in} - V_{out})$', color='slategray',
         fontsize=7)
plt.savefig('filtroPB.png')
plt.show()


#csv

dic = {'tempi': tt,'Vin': vin,'Vout1': vv0[:,0],'Vout0.1': vv1[:,0],'Vout0.01': vv2[:,0]}
df = pd.DataFrame(data=dic)
df.to_csv('DataFrameFiltro.csv')
