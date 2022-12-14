import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import reco

def arrayHit(tab):
    aa = np.empty(0)
    time = tab['hit_time'].values
    mod = tab['mod_id'].values
    sens = tab['det_id'].values
    for i in range(len(time)):
        aa = np.append(aa, np.array([reco.Hit(mod[i], sens[i], time[i]) ]))
    return aa

def arrayEventi(aHit, threshold):
    aEve = np.array( [reco.Event()] )
    tHitPrec = -1000000
    for i in range(len(aHit)):
        if ( (aHit[i].tempo - tHitPrec) > threshold ) :
            aEve = np.append(aEve, reco.Event())
        aEve[-1].addHit(aHit[i])
        tHitPrec = aHit[i].tempo
            
    return aEve


### Evventi del modulo0
tab = pd.read_csv('hit_times_M0.csv')
#print(tab)
'''
time = tab['hit_time'].values
plt.hist(time, bins=80, color='darkgreen')
plt.show()

time_diff = np.diff(time)
mask = time_diff > 0

plt.hist(np.log10(time_diff[mask]), bins=70, color='darkred')
plt.title('hit provenienti dal modulo 0')
plt.xlabel('log10 della differenza di tempi tra Hit e successivo (ns)')
plt.xlabel('Numero Hit')
plt.savefig('modulo0eventi.png')
plt.show()
'''
  
### Eventi di tutti i moduli

a0 = arrayHit(tab) #array_hit(pd.read_csv('hit_times_M0.csv'))
a1 = arrayHit(pd.read_csv('hit_times_M1.csv'))
a2 = arrayHit(pd.read_csv('hit_times_M2.csv'))
a3 = arrayHit(pd.read_csv('hit_times_M3.csv'))

aaa = np.empty(0)
aaa = np.concatenate((a0, a1, a2, a3))
#print(aaa.shape)
aaa = np.sort(aaa)

aaaTempo = np.array([h.tempo for h in aaa])
aaaModulo = np.array([h.modulo for h in aaa])
aaaSensore = np.array([h.sensore for h in aaa])

print(aaaTempo, aaaModulo, aaaSensore)
aaa_tdiff = (np.diff(aaa)).astype(np.float64)

mask = aaa_tdiff > 0
aaa_dtime = np.log10(aaa_tdiff[mask])

plt.hist(aaa_dtime, bins=30, color='darkcyan')
plt.title('hit provenienti da tutti i moduli')
plt.xlabel(r'$log10(\delta t)$ (ns)')
plt.xlabel('Numero Hit')
plt.savefig('Modulo0123Eventi.png')
plt.show()

aEve = arrayEventi(aaa, 10**(2.2))
print('number of total events ', len(aEve)) 

for i in range(10):
    print(f'-------Event{i}-------', '\n',
          'hit\'s num = ', '\n',
          '-----Evento0-----', '\n',
          '-----Evento0-----', '\n',
          '-----Evento0-----', '\n',
          )
