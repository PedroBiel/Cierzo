# -*- coding: utf-8 -*-
"""
CIERZO CTE DB SE-AE
Controlador de la gráfica de la presión estática

Created on Tue Apr 14 12:29:51 2020

__author__ = Pedro Biel
__version__ = 1.0.0
__email__ = structural.eng.biel@gmail.com
"""


import pandas as pd


from CTE.datos.alturas_sobre_terreno import AlturasSobreTerreno
from CTE.datos.coeficientes_exposicion import CoeficientesExposicion
from CTE.datos.presiones_estaticas import PresionesEstaticas


class CntGrafica:
    """Controlador de la gráfica de la presión estática."""
    
    def __init__(self, ventana):
        self.v = ventana
        
    # Gráfica.
    # ========
    
    def dibuja_grafica(self):
        self.comprueba_datos()
        self.v.z_1 = self.alturas()
        self.v.ce_1 = self.coeficiente_exposicion()
        self.v.qe_1 = self.presion_estatica()
        self.v.df_1 = self.data_frame_resultados()
        self.v.salida_grafica()
        
    
    def comprueba_datos(self):
        """Comprueba que están todos los datos necesarios."""
        
        self.v.h = self.v.lne_altura.text()
        self.v.p = self.v.lne_paso.text()
        
        if (self.v.h == '') or (self.v.p == ''):
            self.v.message_box()
    
    def alturas(self):
        """
        Lista de las alturas sobre el tarreno a pasos de 1 m hasta la altura
        máxima sobre el terreno.
        """
        
        self.v.h = int(self.v.lne_altura.text())
        self.p = 1
        
        alturas_sobre_terreno = AlturasSobreTerreno(self.v.h, self.p)
        z = alturas_sobre_terreno.alturas_z()
        
        return z
    
    def coeficiente_exposicion(self):
        """
        Lista de los coeficientes de exposición en las alturas sobre el terreno
        a cada paso de 1 m.
        """
        
        coef_exposicion = CoeficientesExposicion(
            self.v.k, self.v.L, self.v.Z, self.v.z_1
            )
        ce = coef_exposicion.coeficientes_exposicion_ce()
        
        return ce
    
    def presion_estatica(self):
        """
        Lista de las presiones estáticas en las alturas sobre el terreno a cada
        paso de 1 m.
        """
        
        p_estatica = PresionesEstaticas(
            self.v.qb, self.v.ce_1, self.v.cc, self.v.cp
            )
        qe = p_estatica.presiones_estaticas_qe()
        
        return qe
    
    def data_frame_resultados(self):
        """Pandas DataFrame con los resultados para la gráfica."""
        
        df = pd.DataFrame()
        df['z [m]'] = self.v.z_1
        df['q.e [kN/m²]'] = self.v.qe_1
        
        return df
