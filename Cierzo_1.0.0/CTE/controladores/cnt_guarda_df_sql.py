 # -*- coding: utf-8 -*-
"""
CIERZO CTE DB SE-AE
Controlador de guardar datos de pandas DataFrame a SQLite

Created on Tue Apr 21 12:03:00 2020

__author__ = Pedro Biel
__version__ = 1.0.0
__email__ = structural.eng.biel@gmail.com
"""


import pandas as pd
import sqlite3


from CTE.datos.constantes import Constantes

from CTE.pyqt5_clases.qfiledialog import FileDialog

from CTE.transferencia_datos.pandasdfsqlite import PandasDFSQLite


class CntGuardaDFSQL:
    """Controlador de guardar datos de pandas DataFrame a SQLite."""
    
    def __init__(self, ventana):
        self.v = ventana
    
    def data_frame_datos(self):
        """Pandas DataFrame con todos los datos."""
        
        df = pd.DataFrame()
        df['z_(m)'] = self.v.z
        df['Zona'] = self.v.zona
        df['v.b_(m/s)'] = self.v.vb
        df['q.b_(kN/m²)'] = self.v.qb
        df['pr_(años)'] = self.v.pr
        df['cc'] = self.v.cc
        df['Grado'] = self.v.grado
        df['k'] = self.v.k
        df['L'] = self.v.L
        df['Z'] = self.v.Z
        df['c.e'] = self.v.ce
        df['c.p'] = self.v.cp
        df['q.e (kN/m²)'] = self.v.qe
        df['Ratios'] = self.v.ratio
        
        return df
    
    def data_frame_proyecto(self):
        """Pandas DataFrame con los datos de proyecto."""
        
        proyecto = self.v.dlg_proyecto
        dcc = proyecto.proyecto()
        ser = pd.Series(dcc)
        df = ser.to_frame()
        df = df.T
        
        return df

    def ruta_db(self):
        """Ruta de la base de datos."""

        subtitulo = Constantes.GUARDAR_DATOS
        pfad = FileDialog(subtitulo, '', 'Tipo de ficheros (*.db)')
        ruta_db = pfad.get_save_file_name()

        return ruta_db
    
    def df_sqlite(self):
        """Base de datos SQLite con los datos del DataFrame.""" 
                
        df_datos = self.data_frame_datos()
        df_proyecto = self.data_frame_proyecto()
        
        if df_datos.empty or df_proyecto.empty:
            self.v.message_box()
            
        else:
            ruta = self.ruta_db()
            
            try:
                df_sql = PandasDFSQLite(ruta, df_datos, 'CTE')
                df_sql.df_to_sql()
                df_sql = PandasDFSQLite(ruta, df_proyecto, 'Proyecto')
                df_sql.df_to_sql()
            
            except sqlite3.Error as e:
                print('Error: {}'.format(e))
                self.v.message_box()
        
