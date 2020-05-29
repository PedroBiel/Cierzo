# -*- coding: utf-8 -*-
"""
CIERZO

Created on 12.03.2020

__author__ = Pedro Biel
__version__ = 1.0.0
__email__ = structural.eng.biel@gmail.com
"""


import matplotlib.pyplot as plt
import pandas as pd
import qdarkstyle
import sys

from math import ceil

from PyQt5 import uic
from PyQt5.QtCore import QLibraryInfo, QLocale, QStringListModel, Qt, QTranslator
from PyQt5.QtGui import QFont, QIcon, QIntValidator
# from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableView
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView

from dlg_proyecto.proyecto import DlgProyecto
from dlg_version.version import DlgVersion
from dlg_web.web import DlgWeb

from CTE.controladores.cnt_presion_dinamica import CntPresionDinamica
from CTE.controladores.cnt_periodo_retorno import CntPeriodoRetorno
from CTE.controladores.cnt_coeficientes_entorno import CntCoeficientesEntorno
from CTE.controladores.cnt_presion_estatica import CntPresionEstatica
from CTE.controladores.cnt_grafica import CntGrafica
from CTE.controladores.cnt_excel import CntExcel
from CTE.controladores.cnt_guarda_df_sql import CntGuardaDFSQL
from CTE.controladores.cnt_abre_sql_df import CntAbreSQLDF

from CTE.modelos.tablemodel import PandasModel

from CTE.pyqt5_recipes.messagebox import MessageBox


class MainWindow(QMainWindow):

    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent)
        uic.loadUi('vistas/cierzo_1.ui', self)
        
        self.setWindowIcon(QIcon("iconos/Air.png"))
        
        # Entorno virtual.
        # ================
        print('\n Entorno virtual: \n', sys.prefix)

        # ####################################################################
        
        # MENÚ
        # ====
        
        # Archivo-Proyecto.
        # =================
        self.axn_abrir = self.actionAbrir
        self.axn_guardar = self.actionGuardar
        self.axn_proyecto = self.actionProyecto
        self.axn_about = self.actionAcerca_de_Cierzo
        self.axn_version = self.actionRevisiones
    
        # Eventos.
        # ========
        self.axn_proyecto.triggered.connect(self.dlg_proyecto)
        self.axn_about.triggered.connect(self.call_dialog_web)
        self.axn_version.triggered.connect(self.call_dialog_version) 
        
        # ####################################################################

        # CTE DB SE-AE 2009
        # =================

        # Objetos de la aplicación.
        # =========================
        self.zona = ''  # Zona geográfica.
        self.vb = ''  # [m/s] Velocidad básica.
        self.qb = ''  # [kN/m²] Presión dinámica.
        self.pr = ''  # [años] Periodo de retorno.
        self.cc = ''  # Coeficiente corrector.
        self.grado = ''  # Grado de aspereza del entorno.
        self.defin = ''  # Definición del grado de aspereza.
        self.k = ''  # Parámetro k.
        self.L = ''  # [m] Parámetro L.
        self.Z = ''  # [m] Parámetro Z.
        self.h = ''  # [m] Altura sobre el terreno.
        self.p = ''  # [m] Pasos entre la altura.
        self.z = []  # [m] Alturas de los pasos sobre el terreno.
        self.ce = []  # Coeficiente de exposición.
        self.cp = 1.0  # Coeficiente eólico.
        self.qe = []  # [kN/m²] Presión estática.
        self.qe_10m = ''  # [kN7m²] Presión estática a 10 m de altura.
        self.ratio = ''  # Ratio de presiones estáticas.
        self.df = pd.DataFrame()  # Pandas DataFrame con los resultados.
        self.z_1 = []  # [m] Alturas de los pasos de 1 m sobre el terreno para la gráfica.
        self.ce_1 = []  # Coeficiente de exposición para la gráfica.
        self.qe_1 = []  # [kN/m²] Presión estática para la gráfica.
        self.df_1 = pd.DataFrame()  # Pandas DataFrame con los resultados para la gráfica.
        self.grafica = 'grafica.png'  # Imagen de la gráfica para incorporarla a Excel.
        
        # Instancias de clases.
        # =====================
        self.dlg_proyecto = DlgProyecto(self)
        self.dlg_web = DlgWeb(self)
        self.dlg_version = DlgVersion(self)
        self.cnt_pres_din = CntPresionDinamica(self)
        self.cnt_per_ret = CntPeriodoRetorno(self)
        self.cnt_coef_ent = CntCoeficientesEntorno(self)
        self.cnt_pres_est = CntPresionEstatica(self)
        self.cnt_grafica = CntGrafica(self)
        self.cnt_excel = CntExcel(self)
        self.cnt_guardar = CntGuardaDFSQL(self)
        self.cnt_abrir = CntAbreSQLDF(self)
        
        # Objetos PyQt.
        # =============
        
        # Presión dinámica.
        self.cbx_zona = self.comboBox_zona  # Zona.
        # self.cbx_zona.setEditable(True)
        # self.ledit = self.cbx_zona.lineEdit()
        # self.ledit.setAlignment(Qt.AlignCenter)
        # self.ledit.setReadOnly(True)
        # self.ledit.setStyleSheet("background-color: black;")
        self.lne_vb = self.lineEdit_vb  # Velocidad básica.
        self.lne_vb.setEnabled(False)
        self.lne_vb.setAlignment(Qt.AlignCenter)
        self.lne_vb.setStyleSheet('color: white')
        self.lne_qb = self.lineEdit_qb  # Presión dinámica.
        self.lne_qb.setEnabled(False)
        self.lne_qb.setAlignment(Qt.AlignCenter)
        self.lne_qb.setStyleSheet('color: white')
        
        # Periodo de retorno.
        self.cbx_pr = self.comboBox_pr  # Periodo de retorno.
        self.lne_cc = self.lineEdit_cc  # Coeficiente corrector.
        self.lne_cc.setEnabled(False)
        self.lne_cc.setAlignment(Qt.AlignCenter)
        self.lne_cc.setStyleSheet('color: white')
        
        # Coeficientes de entorno.
        self.cbx_grado = self.comboBox_ga  # Grado de aspereza.
        self.lbl_definicion = self.label_definicion
        self.lbl_definicion.setWordWrap(True)  # Label en múltiples líneas.
        self.lne_k = self.lineEdit_k  # Parámetro k.
        self.lne_k.setEnabled(False)
        self.lne_k.setAlignment(Qt.AlignCenter)
        self.lne_k.setStyleSheet('color: white')
        self.lne_L = self.lineEdit_L  # Parámetro L.
        self.lne_L.setEnabled(False)
        self.lne_L.setAlignment(Qt.AlignCenter)
        self.lne_L.setStyleSheet('color: white')
        self.lne_Z = self.lineEdit_Z  # Parámetro Z.
        self.lne_Z.setEnabled(False)
        self.lne_Z.setAlignment(Qt.AlignCenter)
        self.lne_Z.setStyleSheet('color: white')
        
        # Presión estática.
        self.lne_altura = self.lineEdit_altura
        self.lne_altura.setAlignment(Qt.AlignCenter)
        validator_altura = QIntValidator(0, 200, self)
        self.lne_altura.setValidator(validator_altura)
        self.lne_paso = self.lineEdit_paso
        self.lne_paso.setAlignment(Qt.AlignCenter)
        validator_paso = QIntValidator(0, 50, self)
        self.lne_paso.setValidator(validator_paso)
        self.btn_tabla = self.pushButton_tabla
        self.btn_grafica = self.pushButton_grafica
        self.btn_excel = self.pushButton_excel
        self.btn_abrir = self.pushButton_abrir
        self.btn_guardar = self.pushButton_guardar
        
        # QTableView.
        self.tableview = QTableView()

        # Diccionarios.
        # =============
        self.df_presion_dinamica = \
            self.cnt_pres_din.dataframe_presion_dinamica()
        self.df_periodo_retorno = \
            self.cnt_per_ret.dataframe_periodo_retorno()
        self.df_coeficientes_entorno = \
            self.cnt_coef_ent.dataframe_coeficientes_entorno()
            
        print(self.df_presion_dinamica)
        print(self.df_periodo_retorno)
        print(self.df_coeficientes_entorno)
        
        # Añade items a QComboBox.
        # ========================
        lista_zonas = self.df_presion_dinamica.zonas
        model = QStringListModel(lista_zonas)
        self.cbx_zona.setModel(model)
        
        lista_periodos_retorno = self.df_periodo_retorno.periodo_retorno
        model = QStringListModel(lista_periodos_retorno)
        self.cbx_pr.setModel(model)
        self.cbx_pr.setCurrentIndex(5)
        
        lista_grados = self.df_coeficientes_entorno.grados
        model = QStringListModel(lista_grados)
        self.cbx_grado.setModel(model)
        
        # Añade ítems a QLineEdit.
        # ========================
        self.zona = 'A'
        self.vb = 26
        self.qb = 0.42
        self.lne_vb.setText(str(self.vb))
        self.lne_qb.setText(str(self.qb))
        print()
        print('zona            :', self.zona)
        print('velocidad básica:', self.vb)
        print('presión dinámica:', self.qb)
        
        self.pr = 50
        self.cc = 1.0
        self.lne_cc.setText(str(self.cc))
        print()
        print('periodo de retorno   :', '50')
        print('coeficiente corrector:', self.cc)
        
        self.grado = 'I'
        self.defin = 'Borde del mar o de un lago, con una superficie de agua \
en la dirección del viento de al menos 5 km de longitud.'
        self.k = 0.156
        self.L = 0.003
        self.Z = 1.0
        self.lne_k.setText(str(self.k))
        self.lne_L.setText(str(self.L))
        self.lne_Z.setText(str(self.Z))
        print()
        print('grado      :', self.grado)
        print('definición :', self.defin)
        print('parámetro k:', self.k)
        print('parámetro L:', self.L)
        print('parámetro Z:', self.Z)
        
        # Añade texto a QLabel.
        # =====================
        fuente_lbl = QFont()
        fuente_lbl.setFamily('Consolas')
        fuente_lbl.setPointSize(8)
        self.lbl_definicion.setFont(fuente_lbl)
        self.lbl_definicion.setText(self.defin)

        # Eventos.
        # ========
        
        # Presión dinámica inicial.
        # -------------------------
        self.cbx_zona.currentIndexChanged.connect(
            self.cnt_pres_din.calcula_presion_dinamica
            )
        
        # Periodo de retorno.
        # -------------------
        self.cbx_pr.currentIndexChanged.connect(
            self.cnt_per_ret.calcula_periodo_retorno
            )
        
        # Coeficientes de entorno.
        # ------------------------
        self.cbx_grado.currentIndexChanged.connect(
            self.cnt_coef_ent.calcula_coeficientes_entorno
            )
        
        # Presión estática.
        # ----------------- 
        self.btn_tabla.clicked.connect(
            self.cnt_pres_est.calcula_presion_estatica
            )
        
        # Gráfica.
        # --------
        self.btn_grafica.clicked.connect(
            self.cnt_grafica.dibuja_grafica
            )
        
        # Excel.
        # ------
        # 1. Calcula la presión estática.
        self.btn_excel.clicked.connect(
            self.cnt_pres_est.calcula_presion_estatica
            )
        # 2. Guarda los datos.
        self.btn_excel.clicked.connect(self.cnt_excel.exporta_excel)
        
        # Guardar.
        # --------
        # 1. Calcula la presión estática.
        self.axn_guardar.triggered.connect(
            self.cnt_pres_est.calcula_presion_estatica
            )
        self.btn_guardar.clicked.connect(
            self.cnt_pres_est.calcula_presion_estatica
            )
        # 2. Guarda los datos.
        self.axn_guardar.triggered.connect(
            self.cnt_guardar.df_sqlite
            )
        self.btn_guardar.clicked.connect(
            self.cnt_guardar.df_sqlite
            )

        # Abrir.
        # ------
        self.axn_abrir.triggered.connect(
            self.cnt_abrir.sqlite_df
            )
        self.btn_abrir.clicked.connect(
            self.cnt_abrir.sqlite_df
            )
        
        # ####################################################################

    # ########################################################################

    # MENÚ
    # ====

    def dlg_proyecto(self):
        print('dlg_proyecto')
        self.dlg_proyecto.show()
        
    def call_dialog_web(self):
        """Call the Dialog Web."""

        self.dlg_web.show()
    
    def call_dialog_version(self):
        """Call the Dialog Version."""

        self.dlg_version.show()
        
    # ########################################################################
        
    # CTE DB SE-AE 2009
    # =================

    # Salidas PyQt5.
    # ==============
    def salida_presion_dinamica(self):
        self.lne_vb.setText(str(self.vb))
        self.lne_qb.setText(str(self.qb))
        print()
        print('zona            :', self.zona)
        print('velocidad básica:', self.vb)
        print('presión dinámica:', self.qb)
        
    def salida_coeficiente_corrector(self):
        self.lne_cc.setText(str(self.cc))
        print()
        print('periodo de retorno   :', self.pr)
        print('coeficiente corrector:', self.cc)
        
    def salida_coeficientes_entorno(self):
        self.lbl_definicion.setText(self.defin)
        self.lne_k.setText(str(self.k))
        self.lne_L.setText(str(self.L))
        self.lne_Z.setText(str(self.Z))
        print()
        print('grado      :', 'I')
        print('definición :', self.defin)
        print('parámetro k:', self.k)
        print('parámetro L:', self.L)
        print('parámetro Z:', self.Z)
        
    def salida_presion_estatica(self):
        model = PandasModel(self.df)
        self.tableview.setModel(model)
        self.tableview.setWindowTitle('Resultados de la presión estática')
        self.tableview.resize(515, 260)
        self.tableview.show()
        
    def salida_grafica(self):
        plt.style.use('seaborn-whitegrid')
        print(self.df_1)
        x_max = self.df_1['q.e [kN/m²]'].loc[
            self.df_1['z [m]'] == self.h
            ].values.item()
        x_max = ceil(x_max)
        xlim = [0, x_max]
        ylim = [0, self.h]
        self.df_1.plot(
            kind='line',
            x='q.e [kN/m²]',
            y='z [m]',
            xlim=xlim,
            ylim=ylim,
            legend=False,
            grid=True
            )
        plt.xlabel('$q_e$ [kN/m²]')
        plt.ylabel('$z$ [m]')
        plt.savefig(self.grafica)
        plt.show();
        
    def salida_datos_abiertos(self):
        
        # Salida de la presión dinámica.
        index = self.cbx_zona.findText(self.zona, Qt.MatchFixedString)
        if index >= 0:
             self.cbx_zona.setCurrentIndex(index)
        
        self.lne_vb.setText(str(self.vb))
        self.lne_qb.setText(str(self.qb))
        
        # Salida del coeficiente corrector.
        index = self.cbx_pr.findText(self.pr, Qt.MatchFixedString)
        if index >= 0:
             self.cbx_pr.setCurrentIndex(index)
        
        self.lne_cc.setText(str(self.cc))
        
        # Salida de los coeficientes de entorno.
        index = self.cbx_grado.findText(self.grado, Qt.MatchFixedString)
        if index >= 0:
             self.cbx_grado.setCurrentIndex(index)
        
        self.lbl_definicion.setText(self.defin)
        self.lne_k.setText(str(self.k))
        self.lne_L.setText(str(self.L))
        self.lne_Z.setText(str(self.Z))
        
        # Salida de la presión estática.
        self.lne_altura.setText(str(self.h))
        self.lne_paso.setText(str(self.p))
        
        
    def message_box(self):
        """https://www.tutorialspoint.com/pyqt/pyqt_qmessagebox.htm"""
        
        window_title = 'Advertencia'
        text = 'Faltan datos por introducir.'
        info_text = 'Comprueba de nuevo las entradas de datos.'
        self.messagebox = MessageBox(window_title, text, info_text)
        self.messagebox.warning()
        
    def message_box_db(self):
        """https://www.tutorialspoint.com/pyqt/pyqt_qmessagebox.htm"""
        
        window_title = 'Advertencia'
        text = 'Hay un problema con la base de datos.'
        info_text = 'Comprueba de nuevo las entradas de datos.'
        self.messagebox = MessageBox(window_title, text, info_text)
        self.messagebox.warning()

    # ########################################################################
        

if __name__ == '__main__':

    app = QApplication(sys.argv)

    # Traducir el idiona del sistema operativo y texto predeterminado de PyQt.
    qt_translator = QTranslator()
    qt_translator.load(
        'qtbase_' + QLocale.system().name(),
        QLibraryInfo.location(QLibraryInfo.TranslationsPath)
        )
    app.installTranslator(qt_translator)

    # Dark style.
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    # Fuente.
    fuente = QFont()
    fuente.setFamily('Consolas')
    fuente.setPointSize(11)
    app.setFont(fuente)

    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
