 # -*- coding: utf-8 -*-
"""
CIERZO CTE DB SE-AE
Controlador de abrir datos de SQLite y pasarlos a pandas DataFrame

Created on Tue Mar 21 18:24:00 2020

__author__ = Pedro Biel
__version__ = 1.0.0
__email__ = structural.eng.biel@gmail.com
"""


import pandas as pd
import sqlite3

from CTE.datos.constantes import Constantes
from CTE.datos.diccionarios import Diccionarios

from CTE.pyqt5_clases.qfiledialog import FileDialog

from CTE.transferencia_datos.sqlitepandasdf import SQLitePandasDF


class CntAbreSQLDF:
    """Controlador de abrir datos de SQLite y pasarlos a pandas DataFrame."""
    
    def __init__(self, ventana):
        self.v = ventana
    
    def sqlite_df(self):
        """DataFrame con los datos de la base de datos SQLite."""
        
        ruta_db = self.ruta_db()
        
        try:
            sql_df = SQLitePandasDF(ruta_db, 'CTE')
            self.v.df = sql_df.sql_to_df()
        
        except sqlite3.Error as e:
            print('Error: {}'.format(e))
            self.v.message_box_db()
        
        self.salida_datos()
        
        return self.v.df

    def ruta_db(self):
        """Ruta y nombre de la base de datos."""

        subtitulo = Constantes.ABRIR_DATOS
        pfad = FileDialog(subtitulo, '', 'Tipo de ficheros (*.db)')
        ruta_db = pfad.get_open_file_name()

        return ruta_db


    def salida_datos(self):
        """Dalida de datos PyQt5."""
        
        # Salida de la presión dinámica.
        self.v.zona = self.v.df.iloc[0]['Zona']
        self.v.vb = self.v.df.iloc[0]['v.b_(m/s)']
        self.v.qb = self.v.df.iloc[0]['q.b_(kN/m²)']
        
        # Salida del coeficiente corrector.
        self.v.pr = self.v.df.iloc[0]['pr_(años)']
        self.v.cc = self.v.df.iloc[0]['cc']
        
        # Salida de los coeficientes de entorno.
        self.v.grado = self.v.df.iloc[0]['Grado']
        dcc = Diccionarios.dcc_coeficientes_entorno
        self.v.df_coeficientes_entorno = pd.DataFrame.from_dict(dcc)
        self.v.defin = self.v.df_coeficientes_entorno['definición'].loc[
            self.v.df_coeficientes_entorno['grados'] == self.v.grado
            ].values.item()
        self.v.k = self.v.df.iloc[0]['k']
        self.v.L = self.v.df.iloc[0]['L']
        self.v.Z = self.v.df.iloc[0]['Z']

        # Salida de la presión estática.
        self.v.h = self.v.df['z_(m)'].max()
        self.v.p = self.v.df.iloc[1]['z_(m)'] - self.v.df.iloc[0]['z_(m)']
        
        self.v.salida_datos_abiertos()
