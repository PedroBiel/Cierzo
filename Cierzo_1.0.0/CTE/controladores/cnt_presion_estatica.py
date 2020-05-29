# -*- coding: utf-8 -*-
"""
CIERZO CTE DB SE-AE
Controlador de la presión estática

Created on Tue Mar 24 16:18:51 2020

__author__ = Pedro Biel
__version__ = 1.0.0
__email__ = structural.eng.biel@gmail.com
"""


import numpy as np
import pandas as pd

from CTE.datos.alturas_sobre_terreno import AlturasSobreTerreno
from CTE.datos.coeficientes_exposicion import CoeficientesExposicion
from CTE.datos.presiones_estaticas import PresionesEstaticas
from CTE.datos.ratios_presiones_estaticas import RatiosPresionesEstaticas


class CntPresionEstatica:
    """Controlador de la presión estática."""
    
    def __init__(self, ventana):
        self.v = ventana

    # Valores.
    # ========
    
    def calcula_presion_estatica(self):
        self.comprueba_datos()
        self.v.z = self.alturas()
        self.v.ce = self.coeficiente_exposicion()
        self.v.qe = self.presion_estatica()
        self.v.qe_10m = self.presion_estatica_10_m()
        self.v.ratios = self.ratio_presiones_estaticas()
        self.v.df = self.data_frame_resultados()
        self.v.salida_presion_estatica()

    def comprueba_datos(self):
        """Comprueba que están todos los datos necesarios."""
        
        self.v.h = self.v.lne_altura.text()
        self.v.p = self.v.lne_paso.text()
        print('h:', self.v.h, '\n')
        print(self.v.h == '')
        
        if (self.v.h == '') or (self.v.p == ''):
            self.v.message_box()

    def alturas(self):
        """Lista de las alturas sobre el tarreno a cada paso."""
        
        self.v.h = int(self.v.lne_altura.text())
        self.v.p = int(self.v.lne_paso.text())
        
        alturas_sobre_terreno = AlturasSobreTerreno(self.v.h, self.v.p)
        z = alturas_sobre_terreno.alturas_z()
        
        return z
    
    def coeficiente_exposicion(self):
        """
        Lista de los coeficientes de exposición en las alturas sobre el terreno
        a cada paso.
        """
        
        coef_exposicion = CoeficientesExposicion(
            self.v.k, self.v.L, self.v.Z, self.v.z
            )
        ce = coef_exposicion.coeficientes_exposicion_ce()
        
        return ce
    
    def presion_estatica(self):
        """
        Lista de las presiones estáticas en las alturas sobre el terreno a cada
        paso.
        """
        
        p_estatica = PresionesEstaticas(
            self.v.qb, self.v.ce, self.v.cc, self.v.cp
            )
        qe = p_estatica.presiones_estaticas_qe()
        
        return qe
    
    def presion_estatica_10_m(self):
        """Presión estática a 10 m de altura."""
        
        coef_exposicion_10m = CoeficientesExposicion(
            self.v.k, self.v.L, self.v.Z, 10
            )
        ce_10m = coef_exposicion_10m.coeficiente_exposicion_ce_10m()
        
        p_estatica_10m = PresionesEstaticas(
            self.v.qb, ce_10m, self.v.cc, self.v.cp
            )
        qe_10m = p_estatica_10m.presiones_estaticas_qe()
        
        return qe_10m
    
    def ratio_presiones_estaticas(self):
        """Ratio de las presiones estáticas."""
        
        ratios_qe = RatiosPresionesEstaticas(self.v.qe, self.v.qe_10m)
        self.v.ratio = ratios_qe.ratios()
        
        return self.v.ratio
    
    def data_frame_resultados(self):
        """Pandas DataFrame con los resultados."""
        
        df = pd.DataFrame()
        df['z [m]'] = self.v.z
        df['c.e'] = np.around(self.v.ce, decimals=3)
        df['c.p'] = self.v.cp
        df['q.e [kN/m²]'] = np.around(self.v.qe, decimals=2)
        df['Ratios'] = np.around(self.v.ratios, decimals=2)
        
        return df
