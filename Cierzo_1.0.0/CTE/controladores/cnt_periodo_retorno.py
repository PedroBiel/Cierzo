# -*- coding: utf-8 -*-
"""
CIERZO CTE DB SE-AE
Controlador del periodo de retorno

Created on Fr Mar 20 12:19:53 2020

__author__ = Pedro Biel
__version__ = 1.0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd

from CTE.datos.diccionarios import Diccionarios


class CntPeriodoRetorno:
    """Controlador del periodo de retorno."""
    
    def __init__(self, ventana):
        self.v = ventana

    # DataFrames.
    # ===========

    def dataframe_periodo_retorno(self):
        """DataFrame de pandas del periodo de retorno."""
        
        dcc = Diccionarios.dcc_periodo_retorno        
        self.v.df_periodo_retorno = pd.DataFrame.from_dict(dcc)
        
        return self.v.df_periodo_retorno

    # Valores.
    # ========

    def calcula_periodo_retorno(self):
        self.v.pr = self.periodo_retorno()
        self.v.cc = self.coeficiente_corrector()
        self.v.salida_coeficiente_corrector()

    def periodo_retorno(self):
        """Periodo de retorno."""
        
        pr = self.selecciona_cbx(self.v.cbx_pr)
        
        return pr

    def coeficiente_corrector(self):
        """Coeficiente corrector."""
        
        pr = self.periodo_retorno()
        cc = self.v.df_periodo_retorno['coeficiente_corrector'].loc[
            self.v.df_periodo_retorno['periodo_retorno'] == pr
            ].values.item()
        
        return cc
   
    def selecciona_cbx(self, cbx):
        """Selecciona item del comboBox."""

        current_idx = cbx.currentIndex()
        item = cbx.itemText(current_idx)

        return item




