# -*- coding: utf-8 -*-
"""
CIERZO CTE DB SE-AE
Controlador de exportar datos a Excel

Created on 25.05.2020

__author__ = Pedro Biel
__version__ = 1.0.0
__email__ = structural.eng.biel@gmail.com
"""


import pandas as pd
import time
import xlsxwriter

from CTE.datos.constantes import Constantes

from CTE.pyqt5_clases.qfiledialog import FileDialog


class CntExcel:
    
    def __init__(self, ventana):
        """Controlador de exportar datos a Excel."""
        
        self.v = ventana
    
    def data_frame_proyecto(self):
        """Pandas DataFrame con los datos de proyecto."""
        
        proyecto = self.v.dlg_proyecto
        dcc = proyecto.proyecto()
        ser = pd.Series(dcc)
        df = ser.to_frame()
        df = df.T
        
        return df
    
    def ruta_xlsx(self):
        """Ruta de Excel."""

        subtitulo = Constantes.GUARDAR_DATOS
        pfad = FileDialog(subtitulo, '', 'Tipo de ficheros (*.xlsx)')
        ruta_xlsx = pfad.get_save_file_name()

        return ruta_xlsx

    def exporta_excel(self):
        """Excel con los datos del proyecto y del DataFrame."""
        
        df_proyecto = self.data_frame_proyecto()
        
        if self.v.df.empty or df_proyecto.empty:
            self.v.message_box()
            
        else:
            self.v.cnt_grafica.dibuja_grafica()
            self.exporta_xlsxwriter()

    def exporta_xlsxwriter(self):
        """Crea Excel."""
        
        ruta = self.ruta_xlsx()
        df_proyecto = self.data_frame_proyecto()
        sheet_name = 'Viento CTE'
        
        # Crea un pandas excel writer basado en xlsxwriter.
        # https://stackoverflow.com/questions/30294661/pandas-save-dataframe-to-open-workbook
        writer = pd.ExcelWriter(ruta, engine='xlsxwriter')
        
        # Create a worksheet with an empty dataframe so the sheet is empty.
        dfx = pd.DataFrame()
        dfx.to_excel(writer, sheet_name='Viento CTE')
        
        # Crea libro y hoja nueva.
        wb = writer.book
        wb.set_properties({'title': 'Acción del viento',
                            'subject': 'según CTE DB SE-AE 2009',
                            'author': df_proyecto.iloc[0]['autor']
                            })
        ws = writer.sheets[sheet_name]
        
        # Pie de página.
        footerL = '&L&6&"Monospac821 BT" &F'
        footerR = '&R&6&"Monospac821 BT" &P/&N'
        
        # Formatos.
        format01 = wb.add_format()  # Título.
        format01.set_font_size(18)
        format01.set_bold()
        
        format02 = wb.add_format()  # Negrita alineado izda.
        format02.set_bold()
        format02.set_align('left')
        
        format03 = wb.add_format()  # Alineado centro.
        format03.set_align('center')
        
        format04 = wb.add_format()  # Alineado centro con bordes.
        format04.set_border(1)
        format04.set_align('center')

        
        format05 = wb.add_format()  # Borde inferior.
        format05.set_bottom(1)
        
        format06 = wb.add_format()  # Alineado centro con borde inferior.
        format06.set_align('center')
        format06.set_bottom(1)
        
        format07 = wb.add_format()  # Ajusta el texto a la celda.
        format07.set_text_wrap()
        
        ws.hide_gridlines(2)
        ws.set_footer(footerL + footerR)
        ws.set_column('I:M', 11, format03)
        
        first_row = 3
        first_col = 8
        last_row = first_row + len(self.v.df)
        last_col = first_col + len(self.v.df.columns) - 1
        ws.conditional_format(
            xlsxwriter.utility.xl_range(
                first_row, first_col, last_row, last_col
                ),
            {'type': 'no_errors', 'format': format04}
            )
        
        # Título.
        ws.write('A1', Constantes.D_EXCEL['titulo'], format01)
        ws.write('A2', time.strftime('%d.%m.%Y'))
        
        # Datos de proyecto.
        ws.merge_range('A3:F3', '', format05)
        ws.merge_range('A4:C4', 'Nº de proyecto:')
        ws.merge_range('A5:C5', 'Nombre de proyecto:')
        ws.merge_range('A6:C6', 'Empresa:')
        ws.merge_range('A7:C7', 'Ojeto:')
        ws.merge_range('A8:C8', 'Autor:')
        ws.merge_range('A9:C9', 'Comentario:', format05)
        
        ws.merge_range('D4:F4', df_proyecto.iloc[0]['proyecto'], format02)
        ws.merge_range('D5:F5', df_proyecto.iloc[0]['nombre'], format02)
        ws.merge_range('D6:F6', df_proyecto.iloc[0]['empresa'])
        ws.merge_range('D7:F7', df_proyecto.iloc[0]['objeto'])
        ws.merge_range('D8:F8', df_proyecto.iloc[0]['autor'])
        ws.merge_range('D9:F9', df_proyecto.iloc[0]['comentario'], format05)
        
        # Datos.
        ws.merge_range('A10:F10', '', format05)
        ws.merge_range(
            'A11:C11',
            Constantes.D_EXCEL['subtitulo_presion_dinamica'],
            format02
            )
        ws.merge_range('A12:C12', Constantes.D_EXCEL['zona'])
        ws.merge_range('A13:C13', Constantes.D_EXCEL['vb'])
        ws.merge_range('A14:C14', Constantes.D_EXCEL['qb'], format05)
        ws.merge_range(
            'A15:C15',
            Constantes.D_EXCEL['subtitulo_periodo_retorno'],
            format02
            )
        ws.merge_range('A16:C16', Constantes.D_EXCEL['pr'])
        ws.merge_range('A17:C17', Constantes.D_EXCEL['cc'], format05)
        ws.merge_range(
            'A18:C18',
            Constantes.D_EXCEL['subtitulo_coeficinetes_entorno'],
            format02
            )
        ws.merge_range('A19:C19', Constantes.D_EXCEL['grado'])
        ws.merge_range('A20:F21', self.v.defin, format07)
        ws.merge_range('A22:C22', Constantes.D_EXCEL['k'])
        ws.merge_range('A23:C23', Constantes.D_EXCEL['L'])
        ws.merge_range('A24:C24', Constantes.D_EXCEL['Z'], format05)
        
        ws.write('D13', Constantes.D_EXCEL['vb_simbolo'], format03)
        ws.write('D14', Constantes.D_EXCEL['qb_simbolo'], format06)
        ws.write('D16', Constantes.D_EXCEL['pr_simbolo'], format03)
        ws.write('D17', Constantes.D_EXCEL['cc_simbolo'], format06)
        ws.write('D22', Constantes.D_EXCEL['k_simbolo'], format03)
        ws.write('D23', Constantes.D_EXCEL['L_simbolo'], format03)
        ws.write('D24', Constantes.D_EXCEL['Z_simbolo'], format06)
        
        ws.write('E12', self.v.zona, format03)
        ws.write('E13', self.v.vb, format03)
        ws.write('E14', self.v.qb, format06)
        ws.write('E16', self.v.pr, format03)
        ws.write('E17', self.v.cc, format06)
        ws.write('E19', self.v.grado, format03)
        ws.write('E22', self.v.k, format03)
        ws.write('E23', self.v.L, format03)
        ws.write('E24', self.v.Z, format06)
        
        ws.write('F13', Constantes.D_EXCEL['unidad_m_s'], format03)
        ws.write('F14', Constantes.D_EXCEL['unidad_kN_m2'], format06)
        ws.write('F16', Constantes.D_EXCEL['unidad_anos'], format03)
        ws.write('F17', '', format06)
        ws.write('F23', Constantes.D_EXCEL['unidad_m'], format03)
        ws.write('F24', Constantes.D_EXCEL['unidad_m'], format06)

        # Tabla.
        self.v.df.to_excel(
            writer,
            sheet_name=sheet_name,
            startrow=3,
            startcol=8,
            index=False,
            )

        # Imagen de la gráfica.
        ws.insert_image('O3', self.v.grafica)

        # Cierra libro.
        writer.save()
