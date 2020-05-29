# -*- coding: utf-8 -*-
"""
CIERZO CTE DB SE-AE
Controlador de la presión dinámica

Created on Thu Mar 12 14:49:53 2020

__author__ = Pedro Biel
__version__ = 1.0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd

from CTE.datos.diccionarios import Diccionarios


class CntPresionDinamica:
    """Controlador de la presión dinámica."""
    
    def __init__(self, ventana):
        self.v = ventana

    # DataFrames.
    # ===========

    def dataframe_presion_dinamica(self):
        """DataFrame de pandas de la presión dinámica."""

        dcc = Diccionarios.dcc_presion_dinamica        
        self.v.df_presion_dinamica = pd.DataFrame.from_dict(dcc)
        
        return self.v.df_presion_dinamica

    # Valores.
    # ========

    def calcula_presion_dinamica(self):
        self.v.zona = self.zona()
        self.v.vb = self.velocidad_basica()
        self.v.qb = self.presion_dinamica()
        self.v.salida_presion_dinamica()

    def zona(self):
        """Zona."""
        
        zona = self.selecciona_cbx(self.v.cbx_zona)
        
        return zona

    def velocidad_basica(self):
        """Velocidad básica."""
        
        zona = self.zona()
        vb = self.v.df_presion_dinamica['velocidad_básica'].loc[
            self.v.df_presion_dinamica['zonas'] == zona
            ].values.item()
        
        return vb

    def presion_dinamica(self):
        """Presión dinámica."""
        
        zona = self.zona()
        qb = self.v.df_presion_dinamica['presion_dinámica'].loc[
            self.v.df_presion_dinamica['zonas'] == zona
            ].values.item()
        
        return qb
    
    def selecciona_cbx(self, cbx):
        """Selecciona item del comboBox."""

        current_idx = cbx.currentIndex()
        item = cbx.itemText(current_idx)

        return item
