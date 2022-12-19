import sys
import numpy as np

class Hit():
    """
    Classe per rappresentare gli hit del rivelatore.
    
    Paramtri:
    - Id Modulo
    - Id Sensore
    - Time Stamp rivelazione
    -------------------------------------------
    Metodi:
    - simbolo '<'  -->  ordina in base al tempo di due hit
    - simbolo '-'  -->  fa la differenza dei tempi di due hit
    """
    def __init__(self, module, sensor, time):
        self.module   = module
        self.sensor   = sensor
        self.time     = time

    def __lt__(self, other):
        return self.time < other.time

    def __sub__(self, other):
        return self.time - other.time
    
    def __str__(self):
        return ("{0}, {1}, {2}".format(self.module, self.sensor, self.time))
        

class Event():
    """
    Classe per rappresentare gli eventi del rivelatore.
    
    Paramtri:
    - Numero hit
    - Time Stamp del primo Hit
    - Time Stamp dell'ultimo Hit
    - Durata temporale
    - Array di tutti gli Hit
    -------------------------------------------
    Metodi:
    - add_hit(modulo, sensore, tempo)
    """
    def __init__(self):
        self.nhit      = 0
        self.tfhit     = 0
        self.tlhit     = 0
        self.dt        = 0
        self.ahit      = np.empty(0)

    def addHit(self, h):
        if len(self.ahit) == 0:
            self.tfhit = h.time
        self.tlhit = h.time
        self.dt = self.tlhit-self.tfhit
        self.ahit = np.append(self.ahit, h)
        self.nhit = len(self.ahit)
