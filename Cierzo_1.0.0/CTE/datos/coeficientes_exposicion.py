# -*- coding: utf-8 -*-
"""
DESCRIPCIÓNCIERZO CTE DB SE-AE
Lista de los coeficientes de exposición en las alturas sobre el terreno a cada
paso

Created on Tue Mar 26 15:36:51 2020

__author__ = Pedro Biel
__version__ = 1.0.0
__email__ = structural.eng.biel@gmail.com
"""


import numpy as np


class CoeficientesExposicion:
    """
    Lista de los coeficientes de exposición en las alturas sobre el terreno a 
    cada paso.
    """
    
    def __init__(self, parametro_k, parametro_L, parametro_Z, alturas):
        self.k = parametro_k
        self.L = parametro_L
        self.Z = parametro_Z
        self.z = alturas
        
    def coeficientes_exposicion_ce(self):
        """Lista con los coeficientes de exposición."""
        
        max_z = np.array([max(i, self.Z) for i in self.z])
        F = self.k * np.log(max_z / self.L)
        ce = F * (F + 7 * self.k)
        
        return ce
    
    def coeficiente_exposicion_ce_10m(self):
        """Coeficiente de exposición a 10 m de altura."""
        
        max_z = max(self.z, self.Z)
        F = self.k * np.log(max_z / self.L)
        ce = F * (F + 7 * self.k)
        
        return ce
        
