# -*- coding: utf-8 -*-
"""
DESCRIPCIÓNCIERZO CTE DB SE-AE
Lista de las presiones estáticas en las alturas sobre el terreno a cada paso

Created on Tue Mar 26 16:15:51 2020

__author__ = Pedro Biel
__version__ = 1.0.0
__email__ = structural.eng.biel@gmail.com
"""

class PresionesEstaticas:
    """
    Lista de las presiones estáticas en las alturas sobre el terreno a cada
    paso.
    """
    
    def __init__(
            self,
            presion_dinamica,
            coef_exposicion,
            coef_corrector,
            coef_eolico
            ):
        self.qb = presion_dinamica
        self.ce = coef_exposicion
        self.cc = coef_corrector
        self.cp = coef_eolico
        
    def presiones_estaticas_qe(self):
        """Lista con las presiones estáticas."""
        
        qe = self.qb * self.ce * self.cp * self.cc
        
        return qe
