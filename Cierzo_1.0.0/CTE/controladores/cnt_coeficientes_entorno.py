# -*- coding: utf-8 -*-
"""
CIERZO CTE DB SE-AE
Controlador de los coeficientes de entorno

Created on Fr Mar 20 13:08:53 2020

__author__ = Pedro Biel
__version__ = 1.0.0
__email__ = structural.eng.biel@gmail.com
"""


import pandas as pd

from CTE.datos.diccionarios import Diccionarios


class CntCoeficientesEntorno:
    """Controlador de la presión dinámica."""
    
    def __init__(self, ventana):
        self.v = ventana

    # DataFrames.
    # ===========
      
    def dataframe_coeficientes_entorno(self):
        """DataFrame de pandas de los coeficientes de entorno."""
        
        dcc = Diccionarios.dcc_coeficientes_entorno
        self.v.df_coeficientes_entorno = pd.DataFrame.from_dict(dcc)
        
        return self.v.df_coeficientes_entorno

    # Valores.
    # ========

    def calcula_coeficientes_entorno(self):
        self.v.grado = self.grado()
        self.v.defin = self.definicion()
        self.v.k = self.parametro_k()
        self.v.L = self.parametro_L()
        self.v.Z = self.parametro_Z()
        self.v.salida_coeficientes_entorno()

    def grado(self):
        """Grado de asperza del entorno."""
        
        grd = self.selecciona_cbx(self.v.cbx_grado)
        
        return grd

    def definicion(self):
        """Definición del grado de aspereza."""
        
        grd = self.grado()
        defin = self.v.df_coeficientes_entorno['definición'].loc[
            self.v.df_coeficientes_entorno['grados'] == grd
            ].values.item()
        
        return defin

    def parametro_k(self):
        """Parámetro k."""
        
        grd = self.grado()
        k = self.v.df_coeficientes_entorno['k'].loc[
            self.v.df_coeficientes_entorno['grados'] == grd
            ].values.item()
        
        return k
    
    def parametro_L(self):
        """Parámetro L."""
        
        grd = self.grado()
        L = self.v.df_coeficientes_entorno['L'].loc[
            self.v.df_coeficientes_entorno['grados'] == grd
            ].values.item()
        
        return L
    
    def parametro_Z(self):
        """Parámetro Z."""
        
        grd = self.grado()
        Z = self.v.df_coeficientes_entorno['Z'].loc[
            self.v.df_coeficientes_entorno['grados'] == grd
            ].values.item()
        
        return Z
    
    def selecciona_cbx(self, cbx):
        """Selecciona item del comboBox."""

        current_idx = cbx.currentIndex()
        item = cbx.itemText(current_idx)

        return item
