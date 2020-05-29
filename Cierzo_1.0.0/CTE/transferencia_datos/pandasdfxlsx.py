# -*- coding: utf-8 -*-
"""
Transfiere datos de pandas DataFrame a Excel

Created on Fri Dec 20 11:47:08 2019

__author__ = Pedro Biel
__version__ = 0.0
__email__ = pbiel@taimweser.com
"""


import pandas as pd
import xlsxwriter


class PandasDFXLSX:
    """Transfiere los datos a una hoja de cálculo Excel."""

    def __init__(self, ruta_nombre, df):
        self.ruta_nombre = ruta_nombre  # Ruta y nombre de la hoja de cálculo a guardar.
        self.df = df  # DataFrame a convertir.

    def df_to_excel(self):

        sheet_name = 'Placa base'
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(self.ruta_nombre, engine='xlsxwriter')
        # Convert the dataframe to an XlsxWriter Excel object.
        self.df.to_excel(writer, sheet_name=sheet_name)
        # Get the xlsxwriter workbook and worksheet objects.
        wb = writer.book
        ws = writer.sheets[sheet_name]
        # Add some cell formats.
        format1 = wb.add_format()
        format1.set_align('center')
        # Set the column width and format.
        ws.set_column('B:B', 25, format1)
        ws.set_column('C:C', 10, format1)
        ws.set_column('D:D', 10, format1)
        ws.set_column('E:E', 40, format1)
        ws.set_column('F:F', 20, format1)
        # Close the Pandas Excel writer.
        writer.save()
