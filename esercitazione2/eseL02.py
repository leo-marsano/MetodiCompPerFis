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

giorno = np.arange(1, 31, 1)
temp = np.random.normal( loc=20, scale=5, size=30)
err_temp = np.ones(30)
piogg = np.random.normal( loc=2, scale=2, size=30)
err_piogg = np.ones(30)

df =  pd.DataFrame( columns=['giorni', 'temperatura media', 'err_temp', 'pioggia in mm', 'err_piogg'])

df['giorni'] = giorno
df['temperatura media'] = temp
df['err_temp'] = err_temp
df['pioggia in mm'] = piogg
df['err_piogg'] = err_piogg

df.to_csv('df.csv', index=False)

print(df)


