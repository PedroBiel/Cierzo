# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 17:31:57 2017

@author: Pedro Biel

Wind action according to FEM 2131/2132
"""

import os
import sys
import locale

import logging

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.FEM_2131_2132.chapter_2.loads_0_0_170808 import AdditionalLoads

from qtdesigner.cierzo_0_0_170808 import *

from scripts.py2xlsx_0_0_170808 import py2xlsx
from scripts.py2docx_0_0_170808 import py2docx


locale.setlocale(locale.LC_ALL, '')


class Window(QtGui.QMainWindow):  # QMainWindow instead of QDialog in order to have minimize button.

    def __init__(self, parent=None):

        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.wind_speed_in_service_ms = self.ui.lineEditInServiceSpeed_ms
        self.wind_speed_travelling_ms = self.ui.lineEditTravellingSpeed_ms
        self.wind_speed_out_of_service_to_20_ms = self.ui.lineEditOutOfServiceSpeedTo20_ms
        self.wind_speed_out_of_service_to_100_ms = self.ui.lineEditOutOfServiceSpeedTo100_ms
        self.wind_speed_out_of_service_more_100_ms = self.ui.lineEditOutOfServiceSpeedMore100_ms

        self.wind_speed_in_service_kmh = self.ui.lineEditInServiceSpeed_kmh
        self.wind_speed_travelling_kmh = self.ui.lineEditTravellingSpeed_kmh
        self.wind_speed_out_of_service_to_20_kmh = self.ui.lineEditOutOfServiceSpeedTo20_kmh
        self.wind_speed_out_of_service_to_100_kmh = self.ui.lineEditOutOfServiceSpeedTo100_kmh
        self.wind_speed_out_of_service_more_100_kmh = self.ui.lineEditOutOfServiceSpeedMore100_kmh

        self.wind_load = AdditionalLoads()

        # Open project

        QObject.connect(self.ui.pushButtonOpenProject, QtCore.SIGNAL('clicked()'), self.open_project)

        # Save project

        QObject.connect(self.ui.pushButtonSaveProject, QtCore.SIGNAL('clicked()'), self.save_project)

        # Export to docx

        QObject.connect(self.ui.pushButtonExportDocx, QtCore.SIGNAL('clicked()'), self.export_docx)

        # Export to xlsx

        QObject.connect(self.ui.pushButtonExportXlsx, QtCore.SIGNAL('clicked()'), self.export_xlsx)

        # m/s to km/h

        # Wind speed in service m/s to km/h
        QtCore.QObject.connect(self.ui.lineEditInServiceSpeed_ms,
                               QtCore.SIGNAL('editingFinished()'),
                               self.wind_speed_in_service_ms2kmh)

        # Wind speed travelling m/s to km/h
        QtCore.QObject.connect(self.ui.lineEditTravellingSpeed_ms,
                               QtCore.SIGNAL('editingFinished()'),
                               self.wind_speed_travelling_ms2kmh)

        # Wind speed out of service to 20 m/s to km/h
        QtCore.QObject.connect(self.ui.lineEditOutOfServiceSpeedTo20_ms,
                               QtCore.SIGNAL('editingFinished()'),
                               self.wind_speed_out_of_service_to_20_ms2kmh)

        # Wind speed out of service to 100 m/s to km/h
        QtCore.QObject.connect(self.ui.lineEditOutOfServiceSpeedTo100_ms,
                               QtCore.SIGNAL('editingFinished()'),
                               self.wind_speed_out_of_service_to_100_ms2kmh)

        # Wind speed out of service more than 100 m/s to km/h
        QtCore.QObject.connect(self.ui.lineEditOutOfServiceSpeedMore100_ms,
                               QtCore.SIGNAL('editingFinished()'),
                               self.wind_speed_out_of_service_more_100_ms2kmh)

        # km/h to m/s

        # Wind speed in service km/h to m/s
        QtCore.QObject.connect(self.ui.lineEditInServiceSpeed_kmh,
                               QtCore.SIGNAL('editingFinished()'),
                               self.wind_speed_in_service_kmh2ms)

        # Wind speed travelling km/h to m/s
        QtCore.QObject.connect(self.ui.lineEditTravellingSpeed_kmh,
                               QtCore.SIGNAL('editingFinished()'),
                               self.wind_speed_travelling_kmh2ms)

        # Wind speed out of service to 20 km/h to m/s
        QtCore.QObject.connect(self.ui.lineEditOutOfServiceSpeedTo20_kmh,
                               QtCore.SIGNAL('editingFinished()'),
                               self.wind_speed_out_of_service_to_20_kmh2ms)

        # Wind speed out of service to 100 km/h to m/s
        QtCore.QObject.connect(self.ui.lineEditOutOfServiceSpeedTo100_kmh,
                               QtCore.SIGNAL('editingFinished()'),
                               self.wind_speed_out_of_service_to_100_kmh2ms)

        # Wind speed out of service more than 100 km/h to m/s
        QtCore.QObject.connect(self.ui.lineEditOutOfServiceSpeedMore100_kmh,
                               QtCore.SIGNAL('editingFinished()'),
                               self.wind_speed_out_of_service_more_100_kmh2ms)

    # List with data.

    def data(self):

        data = [self.ui.lineEditProject.text(),
                self.ui.lineEditName.text(),
                self.ui.lineEditCompany.text(),
                self.ui.lineEditAuthor.text(),
                self.ui.textEditComentary.toPlainText(),

                self.ui.lineEditInServiceSpeed_ms.text(),
                self.ui.lineEditInServiceSpeed_kmh.text(),
                self.ui.lineEditInServicePressure.text(),
                self.ui.lineEditInServiceRatio.text(),

                self.ui.lineEditTravellingSpeed_ms.text(),
                self.ui.lineEditTravellingSpeed_kmh.text(),
                self.ui.lineEditTravellingPressure.text(),
                self.ui.lineEditTravellingRatio.text(),

                self.ui.lineEditOutOfServiceSpeedTo20_ms.text(),
                self.ui.lineEditOutOfServiceSpeedTo20_kmh.text(),
                self.ui.lineEditOutOfServicePressureTo20.text(),
                self.ui.lineEditOutOfServiceRatioTo20.text(),

                self.ui.lineEditOutOfServiceSpeedTo100_ms.text(),
                self.ui.lineEditOutOfServiceSpeedTo100_kmh.text(),
                self.ui.lineEditOutOfServicePressureTo100.text(),
                self.ui.lineEditOutOfServiceRatioTo100.text(),

                self.ui.lineEditOutOfServiceSpeedMore100_ms.text(),
                self.ui.lineEditOutOfServiceSpeedMore100_kmh.text(),
                self.ui.lineEditOutOfServicePressureMore100.text(),
                self.ui.lineEditOutOfServiceRatioMore100.text()
                ]

        return data

    # Open project.

    def open_project(self):

        open_file = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '', '*.crz;; All Files (*.*)')

        with open(open_file, 'r') as f:
            data = f.readlines()

        data = [x.strip() for x in data]  # Append the lines to a list and remove '\n' at the end of each line.

        self.ui.lineEditProject.setText(data[0])
        self.ui.lineEditName.setText(data[1])
        self.ui.lineEditCompany.setText(data[2])
        self.ui.lineEditAuthor.setText(data[3])
        self.ui.textEditComentary.setText(data[4])

        self.ui.lineEditInServiceSpeed_ms.setText(str(data[-20]))
        self.ui.lineEditInServiceSpeed_kmh.setText(data[-19])
        self.ui.lineEditInServicePressure.setText(data[-18])
        self.ui.lineEditInServiceRatio.setText(data[-17])

        self.ui.lineEditTravellingSpeed_ms.setText(data[-16])
        self.ui.lineEditTravellingSpeed_kmh.setText(data[-15])
        self.ui.lineEditTravellingPressure.setText(data[-14])
        self.ui.lineEditTravellingRatio.setText(data[-13])

        self.ui.lineEditOutOfServiceSpeedTo20_ms.setText(data[-12])
        self.ui.lineEditOutOfServiceSpeedTo20_kmh.setText(data[-11])
        self.ui.lineEditOutOfServicePressureTo20.setText(data[-10])
        self.ui.lineEditOutOfServiceRatioTo20.setText(data[-9])

        self.ui.lineEditOutOfServiceSpeedTo100_ms.setText(data[-8])
        self.ui.lineEditOutOfServiceSpeedTo100_kmh.setText(data[-7])
        self.ui.lineEditOutOfServicePressureTo100.setText(data[-6])
        self.ui.lineEditOutOfServiceRatioTo100.setText(data[-5])

        self.ui.lineEditOutOfServiceSpeedMore100_ms.setText(data[-4])
        self.ui.lineEditOutOfServiceSpeedMore100_kmh.setText(data[-3])
        self.ui.lineEditOutOfServicePressureMore100.setText(data[-2])
        self.ui.lineEditOutOfServiceRatioMore100.setText(data[-1])

        if len(data) > 25:  # If the length of the data file is more than 25 the commentaries,
                            # field has more than one paragraph.

            extra_paragraphs = len(data) - 25

            for i in range(extra_paragraphs):

                i += 1
                self.ui.textEditComentary.append(data[4 + i])

    # Save project.

    def save_project(self):

        save_file = QtGui.QFileDialog.getSaveFileName(self, 'Save file', '', '*.crz;; All Files (*.*)')

        with open(save_file, 'w') as f:

            f.write(self.ui.lineEditProject.text() + '\n')
            f.write(self.ui.lineEditName.text() + '\n')
            f.write(self.ui.lineEditCompany.text() + '\n')
            f.write(self.ui.lineEditAuthor.text() + '\n')
            f.write(self.ui.textEditComentary.toPlainText() + '\n')

            f.write(self.ui.lineEditInServiceSpeed_ms.text() + '\n')
            f.write(self.ui.lineEditInServiceSpeed_kmh.text() + '\n')
            f.write(self.ui.lineEditInServicePressure.text() + '\n')
            f.write(self.ui.lineEditInServiceRatio.text() + '\n')

            f.write(self.ui.lineEditTravellingSpeed_ms.text() + '\n')
            f.write(self.ui.lineEditTravellingSpeed_kmh.text() + '\n')
            f.write(self.ui.lineEditTravellingPressure.text() + '\n')
            f.write(self.ui.lineEditTravellingRatio.text() + '\n')

            f.write(self.ui.lineEditOutOfServiceSpeedTo20_ms.text() + '\n')
            f.write(self.ui.lineEditOutOfServiceSpeedTo20_kmh.text() + '\n')
            f.write(self.ui.lineEditOutOfServicePressureTo20.text() + '\n')
            f.write(self.ui.lineEditOutOfServiceRatioTo20.text() + '\n')

            f.write(self.ui.lineEditOutOfServiceSpeedTo100_ms.text() + '\n')
            f.write(self.ui.lineEditOutOfServiceSpeedTo100_kmh.text() + '\n')
            f.write(self.ui.lineEditOutOfServicePressureTo100.text() + '\n')
            f.write(self.ui.lineEditOutOfServiceRatioTo100.text() + '\n')

            f.write(self.ui.lineEditOutOfServiceSpeedMore100_ms.text() + '\n')
            f.write(self.ui.lineEditOutOfServiceSpeedMore100_kmh.text() + '\n')
            f.write(self.ui.lineEditOutOfServicePressureMore100.text() + '\n')
            f.write(self.ui.lineEditOutOfServiceRatioMore100.text() + '\n')

    # Export to docx.

    def export_docx(self):

        # Al crear el ejecutable con cx_Freeze no se guardaba el fichero docx. Para detectar el problema se creó el
        # logging y se vió que la línea de código
        # name_py = os.path.basename(__file__)[:-4]
        # no funciona. Se sustituyó por if getattr(...

        logging.info('Abre ventana para guardar docx.')
        name_docx = QtGui.QFileDialog.getSaveFileName(self, 'Save docx', '', '*.docx;; All Files (*.*)')
        logging.info('Abierta ventana para guardar docx.')

        logging.info('Registra nombre de la aplicación.')
        if getattr(sys, 'frozen', False):
            # frozen
            name_py = os.path.basename(sys.executable)[:-4]
        else:
            # unfrozen
            name_py = os.path.basename(os.path.realpath(__file__))[:-4]
        logging.info('Registrado nombre de la aplicación.')

        logging.info('Traspasa datos.')
        data = self.data()
        logging.info('Traspasados datos.')

        logging.info('Ejecuta la función py2docx()')
        py2docx(name_docx, name_py, *data)
        logging.info('Ejecutada la función py2docx()')

    # Export to xlsx.

    def export_xlsx(self):

        name_xlsx = QtGui.QFileDialog.getSaveFileName(self, 'Save xlsx', '', '*.xlsx;; All Files (*.*)')

        if getattr(sys, 'frozen', False):
            # frozen
            name_py = os.path.basename(sys.executable)[:-4]
        else:
            # unfrozen
            name_py = os.path.basename(os.path.realpath(__file__))[:-4]

        data = self.data()

        data_temp1 = [d.split('\n') for d in data]  # Get rid of '\n' between fields.
        data_temp2 = []
        for d in data_temp1:
            data_temp2 = data_temp2 + d
        data = data_temp2

        py2xlsx(name_xlsx, name_py, *data)

    # Basic pressure.

    def basic_pressure(self):

        vs_ms = float(self.wind_speed_in_service_ms.text())
        basic_press = self.wind_load.aerodynamic_wind_pressure(vs_ms)
        return basic_press

    # m/s to km/h.

    def wind_speed_in_service_ms2kmh(self):

        vs_ms = float(self.wind_speed_in_service_ms.text())
        vs_kmh = int(3.6 * vs_ms)

        self.ui.lineEditInServiceSpeed_kmh.setText(str(vs_kmh))

        wind_pressure = self.wind_load.aerodynamic_wind_pressure(vs_ms)
        wind_pressure_ = locale.format('%.2f', wind_pressure)

        self.ui.lineEditInServicePressure.setText(str(wind_pressure_))

        self.ui.lineEditInServiceRatio.setText('1,000')  # Wind pressure in service is the basic pressure.

        # Update ratios.

        self.wind_speed_travelling_ms2kmh()
        self.wind_speed_out_of_service_to_20_ms2kmh()
        self.wind_speed_out_of_service_to_100_ms2kmh()
        self.wind_speed_out_of_service_more_100_kmh2ms()

    def wind_speed_travelling_ms2kmh(self):

        vs_ms = float(self.wind_speed_travelling_ms.text())
        vs_kmh = int(3.6 * vs_ms)

        self.ui.lineEditTravellingSpeed_kmh.setText(str(vs_kmh))

        wind_pressure = self.wind_load.aerodynamic_wind_pressure(vs_ms)
        wind_pressure_ = locale.format('%.2f', wind_pressure)

        self.ui.lineEditTravellingPressure.setText(str(wind_pressure_))

        basic_pressure = self.basic_pressure()
        ratio = wind_pressure / basic_pressure
        ratio_ = locale.format('%.3f', ratio)

        self.ui.lineEditTravellingRatio.setText(str(ratio_))

    def wind_speed_out_of_service_to_20_ms2kmh(self):

        vs_ms = float(self.wind_speed_out_of_service_to_20_ms.text())
        vs_kmh = int(3.6 * vs_ms)

        self.ui.lineEditOutOfServiceSpeedTo20_kmh.setText(str(vs_kmh))

        wind_pressure = self.wind_load.aerodynamic_wind_pressure(vs_ms)
        wind_pressure_ = locale.format('%.2f', wind_pressure)

        self.ui.lineEditOutOfServicePressureTo20.setText(str(wind_pressure_))

        basic_pressure = self.basic_pressure()
        ratio = wind_pressure / basic_pressure
        ratio_ = locale.format('%.3f', ratio)

        self.ui.lineEditOutOfServiceRatioTo20.setText(str(ratio_))

    def wind_speed_out_of_service_to_100_ms2kmh(self):

        vs_ms = float(self.wind_speed_out_of_service_to_100_ms.text())
        vs_kmh = int(3.6 * vs_ms)

        self.ui.lineEditOutOfServiceSpeedTo100_kmh.setText(str(vs_kmh))

        wind_pressure = self.wind_load.aerodynamic_wind_pressure(vs_ms)
        wind_pressure_ = locale.format('%.2f', wind_pressure)

        self.ui.lineEditOutOfServicePressureTo100.setText(str(wind_pressure_))

        basic_pressure = self.basic_pressure()
        ratio = wind_pressure / basic_pressure
        ratio_ = locale.format('%.3f', ratio)

        self.ui.lineEditOutOfServiceRatioTo100.setText(str(ratio_))

    def wind_speed_out_of_service_more_100_ms2kmh(self):

        vs_ms = float(self.wind_speed_out_of_service_more_100_ms.text())
        vs_kmh = int(3.6 * vs_ms)

        self.ui.lineEditOutOfServiceSpeedMore100_kmh.setText(str(vs_kmh))

        wind_pressure = self.wind_load.aerodynamic_wind_pressure(vs_ms)
        wind_pressure_ = locale.format('%.2f', wind_pressure)

        self.ui.lineEditOutOfServicePressureMore100.setText(str(wind_pressure_))

        basic_pressure = self.basic_pressure()
        ratio = wind_pressure / basic_pressure
        ratio_ = locale.format('%.3f', ratio)

        self.ui.lineEditOutOfServiceRatioMore100.setText(str(ratio_))

    # km/h to m/s.

    def wind_speed_in_service_kmh2ms(self):

        vs_kmh = float(self.wind_speed_in_service_kmh.text())
        vs_ms = int(vs_kmh / 3.6)

        self.ui.lineEditInServiceSpeed_ms.setText(str(vs_ms))

        wind_pressure = self.wind_load.aerodynamic_wind_pressure(vs_ms)
        wind_pressure_ = locale.format('%.2f', wind_pressure)

        self.ui.lineEditInServicePressure.setText(str(wind_pressure_))

        basic_pressure = self.basic_pressure()
        ratio = wind_pressure / basic_pressure
        ratio_ = locale.format('%.3f', ratio)

        self.ui.lineEditInServiceRatio.setText(str(ratio_))

        # Update ratios.

        self.wind_speed_travelling_kmh2ms()
        self.wind_speed_out_of_service_to_20_kmh2ms()
        self.wind_speed_out_of_service_to_100_kmh2ms()
        self.wind_speed_out_of_service_more_100_kmh2ms()

    def wind_speed_travelling_kmh2ms(self):

        vs_kmh = float(self.wind_speed_travelling_kmh.text())
        vs_ms = int(vs_kmh / 3.6)

        self.ui.lineEditTravellingSpeed_ms.setText(str(vs_ms))

        wind_pressure = self.wind_load.aerodynamic_wind_pressure(vs_ms)
        wind_pressure_ = locale.format('%.2f', wind_pressure)

        self.ui.lineEditTravellingPressure.setText(str(wind_pressure_))

        basic_pressure = self.basic_pressure()
        ratio = wind_pressure / basic_pressure
        ratio_ = locale.format('%.3f', ratio)

        self.ui.lineEditTravellingRatio.setText(str(ratio_))

    def wind_speed_out_of_service_to_20_kmh2ms(self):

        vs_kmh = float(self.wind_speed_out_of_service_to_20_kmh.text())
        vs_ms = int(vs_kmh / 3.6)

        self.ui.lineEditOutOfServiceSpeedTo20_ms.setText(str(vs_ms))

        wind_pressure = self.wind_load.aerodynamic_wind_pressure(vs_ms)
        wind_pressure_ = locale.format('%.2f', wind_pressure)

        self.ui.lineEditOutOfServicePressureTo20.setText(str(wind_pressure_))

        basic_pressure = self.basic_pressure()
        ratio = wind_pressure / basic_pressure
        ratio_ = locale.format('%.3f', ratio)

        self.ui.lineEditOutOfServiceRatioTo20.setText(str(ratio_))

    def wind_speed_out_of_service_to_100_kmh2ms(self):

        vs_kmh = float(self.wind_speed_out_of_service_to_100_kmh.text())
        vs_ms = int(vs_kmh / 3.6)

        self.ui.lineEditOutOfServiceSpeedTo100_ms.setText(str(vs_ms))

        wind_pressure = self.wind_load.aerodynamic_wind_pressure(vs_ms)
        wind_pressure_ = locale.format('%.2f', wind_pressure)

        self.ui.lineEditOutOfServicePressureTo100.setText(str(wind_pressure_))

        basic_pressure = self.basic_pressure()
        ratio = wind_pressure / basic_pressure
        ratio_ = locale.format('%.3f', ratio)

        self.ui.lineEditOutOfServiceRatioTo100.setText(str(ratio_))

    def wind_speed_out_of_service_more_100_kmh2ms(self):

        vs_kmh = float(self.wind_speed_out_of_service_more_100_kmh.text())
        vs_ms = int(vs_kmh / 3.6)

        self.ui.lineEditOutOfServiceSpeedMore100_ms.setText(str(vs_ms))

        wind_pressure = self.wind_load.aerodynamic_wind_pressure(vs_ms)
        wind_pressure_ = locale.format('%.2f', wind_pressure)

        self.ui.lineEditOutOfServicePressureMore100.setText(str(wind_pressure_))

        basic_pressure = self.basic_pressure()
        ratio = wind_pressure / basic_pressure
        ratio_ = locale.format('%.3f', ratio)

        self.ui.lineEditOutOfServiceRatioMore100.setText(str(ratio_))


if __name__ == '__main__':

    fichero_log = 'file.log'
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s : %(levelname)s : %(message)s',
                        filename=fichero_log,
                        filemode='w')

    app = QtGui.QApplication(sys.argv)
    myapp = Window()
    myapp.show()
    sys.exit(app.exec_())
