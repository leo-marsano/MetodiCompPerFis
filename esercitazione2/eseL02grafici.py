"""


    Creare uno script pyton che crei degli array numpy li inserisca in un dataframe pandas 
e salvi i dati in fromato csv. Gli array da generare sono 5:
        array corrispondnete ai giorni in un mese (1-30);
        2 array corrispondneti alla temperatura media del giorno e al relativo errore;
        2 array corrispondneti ai mm di pioggia del giorno e al relativo errore.
    Creare un secondo script python che legga il file csv precededentemente salvato e produca i seguenti grafici:
        grafico di temepratura e mm di pioggia in funzione del giorno, sullo stesso pannello, senza errori;
        grafico di temperatura e pioggia in funzione del giorno, su pannelli diversi, con errori;
        scatter plot dei mm di pioggia in funzione della temepratura.
    Se rimane tempo, provare a variare estetica e dettagli dei grafici realizzati


"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tab = pd.read_csv('df.csv')
print(tab)

ax1 = tab['giorni']

ay1 = tab['temperatura media']
ay2 = tab['pioggia in mm']

ey1 = tab['err_temp']
ey2 = tab['err_piogg']

plt.errorbar(ax1, ay1, yerr=ey1, fmt='s-', color='limegreen', label='temperatura' )
plt.errorbar(ax1, ay2,  yerr=ey2, fmt='o--',color='violet' , label='pioggia in mm' )

plt.xlabel('giorni')
plt.ylabel('temperatura/pioggia')
plt.legend()
plt.show()


