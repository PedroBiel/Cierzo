# -*- coding: utf-8 -*-
"""
DESCRIPCIÓNCIERZO CTE DB SE-AE
Lista de los ratios de las presiones estáticas

Created on Tu Mar 31 13:38:51 2020

__author__ = Pedro Biel
__version__ = 1.0.0
__email__ = structural.eng.biel@gmail.com
"""


class RatiosPresionesEstaticas:
    """
    Lista de los ratios de las presiones estáticas en las alturas sobre el 
    terreno a cada paso.
    """
    
    def __init__(self, qe, qe_10m):
        self.qe = qe
        self.qe_10m = qe_10m
    
    def ratios(self):
        """Lista con los ratios."""
        
        r = self.qe / self.qe_10m
        
        return r
