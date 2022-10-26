import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

k = 3
m = 300

def V(k, x):
    return k*(x**6)

def T(m, x0, k):
    x = np.arange(0, x0, 0.01)
    inte = 1/(V(k,x0)-V(k,x))**0.5
    T = ((8*m)**0.5)*(integrate.simpson(inte, x))
    return T

print(T(m, 50, k))

x = np.arange(1, 51, 1)
y = np.zeros(len(x))
for i in range(len(x)):
    y[i]=T(m,x[i],k)
    
plt.plot(x, y, color='blue')
plt.title('oscilloscopio', color='blue')
plt.xlabel('x')
plt.ylabel('periodo')
plt.show()

