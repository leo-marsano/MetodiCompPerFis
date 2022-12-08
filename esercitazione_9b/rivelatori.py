import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import reco

def array_hit(tab):
    aa = np.empty(0)
    time = tab['hit_time'].values
    mod = tab['mod_id'].values
    sens = tab['det_id'].values
    for i in range(len(time)):
        aa = np.append(aa, reco.Hit(mod[i], sens[i], time[i]))
    return aa  


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
plt.savefig('modulo0eventi.png')
plt.show()
'''
  
### Eventi di tutti i moduli

a0 = array_hit(tab) #array_hit(pd.read_csv('hit_times_M0.csv'))
a1 = array_hit(pd.read_csv('hit_times_M1.csv'))
a2 = array_hit(pd.read_csv('hit_times_M2.csv'))
a3 = array_hit(pd.read_csv('hit_times_M3.csv'))

aaa = np.empty(0)
aaa = np.concatenate((a0, a1, a2, a3))
#print(aaa.shape)
aaa = np.sort(aaa)
aaa_tdiff = np.diff(aaa)

mask = aaa_tdiff > 0
aaa_dtime = np.zeros(len(aaa_tdiff[mask]))

for i in range(len(aaa_tdiff[mask])):
    aaa_dtime[i] = np.log10((aaa_tdiff[mask])[i])

plt.hist(aaa_dtime, bins=30, color='darkcyan')
plt.title('hit provenienti da tutti i moduli')
plt.savefig('Modulo0123Eventi.png')
plt.show()

