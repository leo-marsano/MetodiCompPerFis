import sys
import numpy as np

class Hit():
    """
    Classe per rappresentare gli hit del rivelatore
    
    Paramtri
    -------------------------------------------
    Id Modulo
    Id Sensore
    Time Stamp rivelazione
    """
    def __init__(self, modulo, sensore, tempo):
        self.modulo  = modulo
        self.sensore = sensore
        self.tempo   = tempo
    
    def __lt__(self, other):
        return self.tempo < other.tempo
        

class Event():
    """
    Classe per rappresentare gli eventi del rivelatore
    
    Paramtri
    -------------------------------------------
    Numero hit
    Time Stamp del primo Hit
    Time Stamp dell'ultimo Hit
    Durata temporale
    Array di tutti gli Hit
    """
    def __init__(self):
        self.nhit      = 0
        self.tfhit     = 0
        self.tlhit     = 0
        self.dt        = 0
        self.ahit      = np.empty(0)

    def add_hit(self, h):
        if ahit.size() == 0:
            self.tfhit = h.tempo
        self.tlhit = h.tempo
        self.dt = self.tlhit-tfhit
        self.ahit = np.append(self.ahit, h)
        self.nhit = len(self.ahit)
