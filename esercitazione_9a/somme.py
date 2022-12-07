import sys
import numpy as np

def somma(n):
    anum = np.arange(n+1)
    return np.sum(anum)

def somma_rad(n):
    anum = np.arange(n+1)
    return np.sum(np.sqrt(anum))
