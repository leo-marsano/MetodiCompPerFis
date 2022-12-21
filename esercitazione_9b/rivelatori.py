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
    tHitPrec = aHit[0].time
    for i in range(len(aHit)):
        if ( (aHit[i].time - tHitPrec) > threshold ) :
            aEve = np.append(aEve, reco.Event())
        aEve[-1].addHit(aHit[i])
        tHitPrec = aHit[i].time        
    return aEve


### Module 0 events
tab = pd.read_csv('hit_times_M0.csv')
#print(tab)
if False:
    time = tab['hit_time'].values
    plt.hist(time, bins=80, color='darkgreen')
    plt.show()
    
    time_diff = np.diff(time)
    mask = time_diff > 0
    
    plt.hist(np.log10(time_diff[mask]), bins=70, color='darkred')
    plt.title('hit provenienti dal modulo 0')
    plt.xlabel(r'$log_{10}(\Delta t)$ (ns)')
    plt.ylabel('Numero Hit')
    plt.savefig('modulo0eventi.png')
    plt.show()

        
  
### All modules' events

a0 = arrayHit(tab) #array_hit(pd.read_csv('hit_times_M0.csv'))
a1 = arrayHit(pd.read_csv('hit_times_M1.csv'))
a2 = arrayHit(pd.read_csv('hit_times_M2.csv'))
a3 = arrayHit(pd.read_csv('hit_times_M3.csv'))

aaa = np.empty(0)
aaa = np.concatenate((a0, a1, a2, a3))
#print(aaa.shape)

aaa = np.sort(aaa)

aaaTime = np.array([h.time for h in aaa])
aaaModule = np.array([h.module for h in aaa])
aaaSensor = np.array([h.sensor for h in aaa])
#print(aaaTime, aaaModule, aaaSensor)

aaa_tdiff = (np.diff(aaa)).astype(np.float64)

mask = aaa_tdiff > 0
aaa_dtime = np.log10(aaa_tdiff[mask])

if False:
    plt.hist(aaa_dtime, bins=30, color='darkcyan')
    plt.title('All modules\' hits')
    plt.xlabel(r'$log_{10}(\Delta t)$ (ns)')
    plt.ylabel('Hits\' number')
    plt.savefig('Modulo0123Eventi.png')
    plt.show()


### Total events number
aEve = arrayEventi(aaa, 10**(2.2))
print('number of total events: ', len(aEve)) 

### Info about first 10 events
for i in range(10):
    print(f'----------------Event{i}----------------', '\n',
          'Hit\'s number = ', aEve[i].nhit, '\n',
          'First hit\'s time stamp = ', aEve[i].tfhit, '(ns)\n',
          'Last hit\'s time stamp = ', aEve[i].tlhit, '(ns)\n',
          'Event\'s time  = ', aEve[i].dt, '(ns)\n',
          'Hit\'s array = [mod sens time]')
    for j in range(len(aEve[i].ahit)): print('\t\t', aEve[i].ahit[j], '\n')


### Hists

aHits4Eve = np.empty(0)
aEvenTime = np.empty(0)
aDeltaTime = np.empty(0)
for i in range(len(aEve)):
    aHits4Eve = np.append(aHits4Eve, len(aEve[i].ahit))
    aEvenTime = np.append(aEvenTime, aEve[i].dt)
    if (i>0) :
        aDeltaTime = np.append(aDeltaTime, aEve[i].tfhit - aEve[i-1].tlhit)

### Hits' number per events' hist
if False:
    plt.hist(aHits4Eve, bins=20, color='darkviolet')
    plt.title('hits\' number per events')
    plt.xlabel('# Hits')
    plt.savefig('hitPerEvento.png')
    plt.show()


### Events' length hist
if False:
    plt.hist(aEvenTime, bins=50, color='salmon')
    plt.title('Event time span')
    plt.xlabel('$t_{span}$ (ns)')
    plt.yscale('log')
    plt.savefig('durataEvento.png')
    plt.show()


### Delta time between consecutive events
if False:
    #mask = aDeltaTime > 0
    plt.hist(np.log10(aDeltaTime), bins=50, color='springgreen')
    plt.title(r'$\Delta t$ between consecutive events')
    plt.xlabel(r'$log_{10}(\Delta t)$ (ns)')
    plt.yscale('log')
    plt.savefig('deltaTimeEventi.png')
    plt.show()


### 2D scatter plot tSpan vs hitNumber
if False:
    plt.scatter(aHits4Eve, aEvenTime, marker='o', color = 'darkorange', alpha=0.1)
    plt.title('Event $t_{span}$ vs hits\' number')
    plt.ylabel('$t_{span}$ (ns)')
    plt.xlabel('# hits per Event')
    plt.savefig('tSpanVsNumHit.png')
    plt.show()

xmod = [-5,  5, -5,  5]
ymod = [ 5,  5, -5, -5]
xdet = [-2.5, 2.5, 0, -2.5,  2.5]
ydet = [ 2.5, 2.5, 0, -2.5, -2.5]
aX = [xm + xd for xm in xmod for xd in xdet]
aY = [ym + yd for ym in ymod for yd in ydet]

aPosHitX = np.empty(0)
aPosHitY = np.empty(0)
aTHit = np.empty(0)


### plasma rappresentation of first 10 events all together (overwritten scatter plot)
if False:
    img,ax = plt.subplots(figsize=(9,8))
    plt.scatter(aX, aY, color='lightgray', s=240, alpha=0.3)
    for i in range(10):
        for h in aEve[i].ahit:
            aPosHitX = np.append(aPosHitX, xmod[h.module]+xdet[h.sensor])
            aPosHitY = np.append(aPosHitY, ymod[h.module]+ydet[h.sensor])
            aTHit = np.append(aTHit, h.time-aEve[i].tfhit)
        plt.scatter(aPosHitX, aPosHitY, s=240, c=aTHit, cmap='plasma_r')
    plt.axvline( 0, color='lightgray')
    plt.axhline( 0, color='lightgray')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.title('graphic rappresentation of first 10 events with time information')
    plt.colorbar( ax=ax, label='Hit $t-t_{start}$ (ns)')
    plt.clim(0, 150)
    plt.savefig('plasmaPlot.png')
    plt.show()        

    
### plasma rappresentation of first 10 events

if True:
    fig,ax = plt.subplots(2 ,5 , figsize=(25, 10))
    for i in range(10):
        aPosHitX = np.empty(0)
        aPosHitY = np.empty(0)
        aTHit = np.empty(0)
        y = 0
        z = i
        if i>4 :
            y = 1
            z = i-5
        ax[y,z].scatter(aX, aY, color='lightgray', s=240, alpha=0.3)
        for h in aEve[i].ahit:
            aPosHitX = np.append(aPosHitX, xmod[h.module]+xdet[h.sensor])
            aPosHitY = np.append(aPosHitY, ymod[h.module]+ydet[h.sensor])
            aTHit = np.append(aTHit, h.time-aEve[i].tfhit)
            jj = ax[y,z].scatter(aPosHitX, aPosHitY, s=240, c=aTHit, cmap='plasma_r')
            ax[y,z].set_title(f'event{i}')
            ax[y,z].axvline( 0, color='lightgray')
            ax[y,z].axhline( 0, color='lightgray')
            ax[y,z].set_xlim(-10, 10)
            ax[y,z].set_ylim(-10, 10)
        
    fig.suptitle('graphic rappresentation of first 10 events with time information')
    fig.colorbar(jj, ax=ax.ravel().tolist(), label='Hit $t-t_{start}$ (ns)')
    jj.set_clim(0, 150)
    #plt.clim(0, 150)
    plt.savefig('plasmaSubplot.png')
    plt.show()        
