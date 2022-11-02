'''
il file di dati fit_data.csv contiene dei valori per le variabili x e y;
A) i valori di  possono essere considerati dei conteggi e seguono la statistica poissoniana;
B) si può ipotizzare che i dati rappresentino una curva lognormale (gaussiana nel logaritmo dei valori di );

creare uno script python che:
A) legga il file di dati fit_data.csv;
B) produca un grafico di  in funzione di  nella forma più appropriata;

creare un secondo script python che:
A) definisca una funzione lognormale da usare per il fit dei dati;
B) legga il file di dati fit_data.csv;
C) esegua il fit dei dati con la funzione lognormale;
D) produca il grafico della funzione di fit ottimizzata sovrapposta ai dati;
E) stampi il valore dei parametri del fit e del chi quadrato
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt

def exp(x, A, mu, sig):
    return A*np.exp(-0.5* ( (np.log(x)-mu) /sig )**2)



### tab
tab = pd.read_csv('fit_data.csv')
print(tab)

ax = np.array(tab['x'])
ay = np.array(tab['y'])
err_y = np.sqrt(ay)

### fit
pstart = np.array([100, 5, 2])
params, params_covariance = opt.curve_fit(exp, ax, ay, sigma=err_y/ay, p0=[pstart])
params1, params1_covariance = opt.curve_fit(exp, ax, ay, p0=[pstart])

print('params con sigma y: ', params, '\nparams senza sigma y: ', params1)
print('params_cov con sigma y: ', params_covariance, '\nparams_cov senza sigma y: ', params1_covariance)
print('errori params con sigma y: \n', np.sqrt(params_covariance.diagonal()), '\nerrori params senza sigma y: \n', np.sqrt(params1_covariance.diagonal()))

y_fit = exp(ax, params[0], params[1], params[2])
y1_fit = exp(ax, params1[0], params1[1], params1[2])

### chi2
n = len(ax)-len(params) # number degrees of freedom
chi2 =  np.sum( (y_fit - ay)**2 /ay )
chi2_1 =  np.sum( (y1_fit - ay)**2 /ay )
chi2_rid = chi2/n
chi2_rid1 = chi2_1/n
print('chi2 senza sigma y: ', chi2, '\nchi2 con sigma y: ', chi2_1,
      '\nchi2 ridotto senza sigma y: ', chi2_rid, '\nchi2 ridotto con sigma y: ',
      chi2_rid1)

### plot
plt.errorbar(ax, ay, err_y, fmt='o', color='darkviolet', label='dati csv')
plt.plot(ax, y_fit, '-',color='darkcyan', alpha=0.8, label='fit con sigma_y')
plt.plot(ax, y1_fit, '-',color='orange', alpha=1, label='fit senza sigma_y')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.xscale('log') #scala logaritmica
plt.show()
