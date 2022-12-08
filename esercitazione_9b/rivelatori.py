import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import reco

'''
### Tab
tab = pd.read_csv('hit_times_M0.csv')
#print(tab)

time = tab['hit_time'].values
plt.hist(time, bins=80, color='darkgreen')
plt.show()

time_diff = np.diff(time)

mask = time_diff > 0
plt.hist(np.log10(time_diff[mask]), bins=50, color='darkred')
plt.show()
plt.savefig('modulo0eventi.png')
'''

def array_hit(tab):
    aa = np.empty(0)
    time = tab['hit_time'].values
    mod = tab['mod_id'].values
    sens = tab['det_id'].values
    for i in range(len(time)):
        aa = np.append(aa, reco.Hit(mod[i], sens[i], time[i]))
    return aa    

a0 = array_hit(pd.read_csv('hit_times_M0.csv'))
a1 = array_hit(pd.read_csv('hit_times_M1.csv'))
a2 = array_hit(pd.read_csv('hit_times_M2.csv'))
a3 = array_hit(pd.read_csv('hit_times_M3.csv'))

#print(a0, a1, a2, a3)

aaa = np.empty(0)
aaa = np.append(aaa, a0)
aaa = np.append(aaa, a1)
aaa = np.append(aaa, a2)
aaa = np.append(aaa, a3)
print(len(aaa), len(a0)+len(a1)+len(a2)+len(a3))

aaa = np.sort(aaa)

