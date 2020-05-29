# -*- coding: utf-8 -*-
"""
DESCRIPCIÓNCIERZO CTE DB SE-AE
Lista de las alturas sobre el terreno a cada paso

Created on Tue Mar 26 12:46:51 2020

__author__ = Pedro Biel
__version__ = 1.0.0
__email__ = structural.eng.biel@gmail.com
"""


import numpy as np


class AlturasSobreTerreno:
    """Lista de las alturas sobre el tarreno a cada paso."""
    
    def __init__(self, altura, paso):
        self.h = altura
        self.p = paso
        
    def alturas_z(self):
        """Lista con las alturas."""
        
        inicio = 0
        final = self.h + self.p
        paso = self.p
        z = np.arange(start=inicio, stop=final, step=paso)
        
        return z
