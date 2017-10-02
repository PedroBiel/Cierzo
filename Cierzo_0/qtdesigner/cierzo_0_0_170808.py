# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cierzo_0_0_170808.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(965, 620)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(965, 620))
        Dialog.setMaximumSize(QtCore.QSize(965, 620))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/Air.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("QMainWindow{\n"
"     background-color: #000044;\n"
"}\n"
"\n"
"QDialog{\n"
"    background-color: #000044;\n"
"}\n"
"\n"
"QLabel{\n"
"    font: 16px consolas;\n"
"    color: cyan;\n"
"}\n"
"\n"
"QLabel#labelTitulo{\n"
"    font: bold 22px;\n"
"}\n"
"\n"
"QLabel#labelHeight{\n"
"    font: 12px;\n"
"}\n"
"\n"
"QLabel#labelInService_kNm2{\n"
"    color: lime;\n"
"}\n"
"\n"
"QLabel#labelTravelling_kNm2{\n"
"    color: lime;\n"
"}\n"
"\n"
"QLabel#labelOutOfServiceTo20_kNm2{\n"
"    color: lime;\n"
"}\n"
"\n"
"QLabel#labelOutOfServiceTo100_kNm2{\n"
"    color: lime;\n"
"}\n"
"\n"
"QLabel#labelOutOfServiceMore100_kNm2{\n"
"    color: lime;\n"
"}\n"
"\n"
"QGroupBox{\n"
"    border: 1px solid blue;\n"
"    margin-top: 0.5em;\n"
"    background-color: #000044;\n"
"    font: 12px consolas;\n"
"    color: cyan;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -6px;\n"
"    left: 10px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border: 1px solid blue;\n"
"    background-color: black;\n"
"    font: 16px consolas;\n"
"    color: cyan;\n"
"}\n"
"\n"
"QLineEdit:focus { \n"
"    border: 1px solid lime;\n"
"}\n"
"\n"
"QLineEdit#lineEditInServicePressure{\n"
"    color: lime;\n"
"}\n"
"\n"
"QLineEdit#lineEditTravellingPressure{\n"
"    color: lime;\n"
"}\n"
"\n"
"QLineEdit#lineEditOutOfServicePressureTo20{\n"
"    color: lime;\n"
"}\n"
"\n"
"QLineEdit#lineEditOutOfServicePressureTo100{\n"
"    color: lime;\n"
"}\n"
"\n"
"QLineEdit#lineEditOutOfServicePressureMore100{\n"
"    color: lime;\n"
"}\n"
"\n"
"QLineEdit#lineEditInServiceRatio{\n"
"    color: yellow;\n"
"}\n"
"\n"
"QLineEdit#lineEditTravellingRatio{\n"
"    color: yellow;\n"
"}\n"
"\n"
"QLineEdit#lineEditOutOfServiceRatioTo20{\n"
"    color: yellow;\n"
"}\n"
"\n"
"QLineEdit#lineEditOutOfServiceRatioTo100{\n"
"    color: yellow;\n"
"}\n"
"\n"
"QLineEdit#lineEditOutOfServiceRatioMore100{\n"
"    color: yellow;\n"
"}\n"
"\n"
"QCheckBox{\n"
"    font: 16px consolas;\n"
"    color: cyan;\n"
"}\n"
"\n"
"QTextEdit{\n"
"    border: 1px solid blue;\n"
"    background-color: black;\n"
"    font: 14px consolas;\n"
"    color: cyan;\n"
"}\n"
"\n"
"QTextEdit:focus { \n"
"    border: 1px solid lime;\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: none;\n"
"    background-color: darkblue;\n"
"    font: 16px consolas;\n"
"    color: cyan;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:  blue;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: midnightblue;\n"
"}"))
        self.labelTitulo = QtGui.QLabel(Dialog)
        self.labelTitulo.setGeometry(QtCore.QRect(20, 10, 471, 31))
        self.labelTitulo.setObjectName(_fromUtf8("labelTitulo"))
        self.groupBoxInService = QtGui.QGroupBox(Dialog)
        self.groupBoxInService.setEnabled(True)
        self.groupBoxInService.setGeometry(QtCore.QRect(340, 60, 601, 101))
        self.groupBoxInService.setObjectName(_fromUtf8("groupBoxInService"))
        self.labelInServiceSpeed = QtGui.QLabel(self.groupBoxInService)
        self.labelInServiceSpeed.setGeometry(QtCore.QRect(22, 30, 181, 21))
        self.labelInServiceSpeed.setObjectName(_fromUtf8("labelInServiceSpeed"))
        self.lineEditInServiceSpeed_ms = QtGui.QLineEdit(self.groupBoxInService)
        self.lineEditInServiceSpeed_ms.setGeometry(QtCore.QRect(23, 60, 51, 21))
        self.lineEditInServiceSpeed_ms.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditInServiceSpeed_ms.setObjectName(_fromUtf8("lineEditInServiceSpeed_ms"))
        self.labelInService_ms = QtGui.QLabel(self.groupBoxInService)
        self.labelInService_ms.setGeometry(QtCore.QRect(82, 60, 31, 21))
        self.labelInService_ms.setObjectName(_fromUtf8("labelInService_ms"))
        self.labelInService_kmh = QtGui.QLabel(self.groupBoxInService)
        self.labelInService_kmh.setGeometry(QtCore.QRect(174, 60, 41, 21))
        self.labelInService_kmh.setObjectName(_fromUtf8("labelInService_kmh"))
        self.lineEditInServiceSpeed_kmh = QtGui.QLineEdit(self.groupBoxInService)
        self.lineEditInServiceSpeed_kmh.setGeometry(QtCore.QRect(115, 60, 51, 21))
        self.lineEditInServiceSpeed_kmh.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditInServiceSpeed_kmh.setObjectName(_fromUtf8("lineEditInServiceSpeed_kmh"))
        self.labelInServicePressure = QtGui.QLabel(self.groupBoxInService)
        self.labelInServicePressure.setGeometry(QtCore.QRect(251, 30, 241, 21))
        self.labelInServicePressure.setObjectName(_fromUtf8("labelInServicePressure"))
        self.labelInService_kNm2 = QtGui.QLabel(self.groupBoxInService)
        self.labelInService_kNm2.setGeometry(QtCore.QRect(306, 60, 51, 21))
        self.labelInService_kNm2.setObjectName(_fromUtf8("labelInService_kNm2"))
        self.lineEditInServicePressure = QtGui.QLineEdit(self.groupBoxInService)
        self.lineEditInServicePressure.setEnabled(False)
        self.lineEditInServicePressure.setGeometry(QtCore.QRect(252, 60, 51, 20))
        self.lineEditInServicePressure.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditInServicePressure.setObjectName(_fromUtf8("lineEditInServicePressure"))
        self.lineEditInServiceRatio = QtGui.QLineEdit(self.groupBoxInService)
        self.lineEditInServiceRatio.setEnabled(False)
        self.lineEditInServiceRatio.setGeometry(QtCore.QRect(520, 60, 61, 20))
        self.lineEditInServiceRatio.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditInServiceRatio.setObjectName(_fromUtf8("lineEditInServiceRatio"))
        self.labelInServiceRatio = QtGui.QLabel(self.groupBoxInService)
        self.labelInServiceRatio.setGeometry(QtCore.QRect(520, 30, 61, 21))
        self.labelInServiceRatio.setObjectName(_fromUtf8("labelInServiceRatio"))
        self.groupBoxOutOfService = QtGui.QGroupBox(Dialog)
        self.groupBoxOutOfService.setGeometry(QtCore.QRect(340, 300, 601, 301))
        self.groupBoxOutOfService.setObjectName(_fromUtf8("groupBoxOutOfService"))
        self.labelHeight = QtGui.QLabel(self.groupBoxOutOfService)
        self.labelHeight.setGeometry(QtCore.QRect(20, 60, 271, 21))
        self.labelHeight.setObjectName(_fromUtf8("labelHeight"))
        self.labelOutOfServiceSpeed = QtGui.QLabel(self.groupBoxOutOfService)
        self.labelOutOfServiceSpeed.setGeometry(QtCore.QRect(20, 30, 181, 21))
        self.labelOutOfServiceSpeed.setObjectName(_fromUtf8("labelOutOfServiceSpeed"))
        self.labelOutOfServiceTo20_kmh = QtGui.QLabel(self.groupBoxOutOfService)
        self.labelOutOfServiceTo20_kmh.setGeometry(QtCore.QRect(180, 120, 41, 21))
        self.labelOutOfServiceTo20_kmh.setObjectName(_fromUtf8("labelOutOfServiceTo20_kmh"))
        self.labelOutOfServiceTo20_ms = QtGui.QLabel(self.groupBoxOutOfService)
        self.labelOutOfServiceTo20_ms.setGeometry(QtCore.QRect(80, 120, 31, 21))
        self.labelOutOfServiceTo20_ms.setObjectName(_fromUtf8("labelOutOfServiceTo20_ms"))
        self.lineEditOutOfServiceSpeedTo20_kmh = QtGui.QLineEdit(self.groupBoxOutOfService)
        self.lineEditOutOfServiceSpeedTo20_kmh.setGeometry(QtCore.QRect(120, 120, 51, 20))
        self.lineEditOutOfServiceSpeedTo20_kmh.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditOutOfServiceSpeedTo20_kmh.setObjectName(_fromUtf8("lineEditOutOfServiceSpeedTo20_kmh"))
        self.lineEditOutOfServiceSpeedTo20_ms = QtGui.QLineEdit(self.groupBoxOutOfService)
        self.lineEditOutOfServiceSpeedTo20_ms.setGeometry(QtCore.QRect(20, 120, 51, 20))
        self.lineEditOutOfServiceSpeedTo20_ms.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditOutOfServiceSpeedTo20_ms.setObjectName(_fromUtf8("lineEditOutOfServiceSpeedTo20_ms"))
        self.lineEditOutOfServiceSpeedTo100_ms = QtGui.QLineEdit(self.groupBoxOutOfService)
        self.lineEditOutOfServiceSpeedTo100_ms.setGeometry(QtCore.QRect(20, 190, 51, 20))
        self.lineEditOutOfServiceSpeedTo100_ms.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditOutOfServiceSpeedTo100_ms.setObjectName(_fromUtf8("lineEditOutOfServiceSpeedTo100_ms"))
        self.lineEditOutOfServiceSpeedTo100_kmh = QtGui.QLineEdit(self.groupBoxOutOfService)
        self.lineEditOutOfServiceSpeedTo100_kmh.setGeometry(QtCore.QRect(120, 190, 51, 20))
        self.lineEditOutOfServiceSpeedTo100_kmh.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditOutOfServiceSpeedTo100_kmh.setObjectName(_fromUtf8("lineEditOutOfServiceSpeedTo100_kmh"))
        self.labelOutOfServiceTo100_ms = QtGui.QLabel(self.groupBoxOutOfService)
        self.labelOutOfServiceTo100_ms.setGeometry(QtCore.QRect(80, 190, 31, 21))
        self.labelOutOfServiceTo100_ms.setObjectName(_fromUtf8("labelOutOfServiceTo100_ms"))
        self.labelOutOfServiceTo100_kmh = QtGui.QLabel(self.groupBoxOutOfService)
        self.labelOutOfServiceTo100_kmh.setGeometry(QtCore.QRect(180, 190, 41, 21))
        self.labelOutOfServiceTo100_kmh.setObjectName(_fromUtf8("labelOutOfServiceTo100_kmh"))
        self.lineEditOutOfServiceSpeedMore100_ms = QtGui.QLineEdit(self.groupBoxOutOfService)
        self.lineEditOutOfServiceSpeedMore100_ms.setGeometry(QtCore.QRect(20, 260, 51, 20))
        self.lineEditOutOfServiceSpeedMore100_ms.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditOutOfServiceSpeedMore100_ms.setObjectName(_fromUtf8("lineEditOutOfServiceSpeedMore100_ms"))
        self.lineEditOutOfServiceSpeedMore100_kmh = QtGui.QLineEdit(self.groupBoxOutOfService)
        self.lineEditOutOfServiceSpeedMore100_kmh.setGeometry(QtCore.QRect(120, 260, 51, 20))
        self.lineEditOutOfServiceSpeedMore100_kmh.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditOutOfServiceSpeedMore100_kmh.setObjectName(_fromUtf8("lineEditOutOfServiceSpeedMore100_kmh"))
        self.labelOutOfServiceMore100_ms = QtGui.QLabel(self.groupBoxOutOfService)
        self.labelOutOfServiceMore100_ms.setGeometry(QtCore.QRect(80, 260, 31, 21))
        self.labelOutOfServiceMore100_ms.setObjectName(_fromUtf8("labelOutOfServiceMore100_ms"))
        self.labelOutOfServiceMore100_kmh = QtGui.QLabel(self.groupBoxOutOfService)
        self.labelOutOfServiceMore100_kmh.setGeometry(QtCore.QRect(180, 260, 41, 21))
        self.labelOutOfServiceMore100_kmh.setObjectName(_fromUtf8("labelOutOfServiceMore100_kmh"))
        self.labelOutOfServiceTo20_kNm2 = QtGui.QLabel(self.groupBoxOutOfService)
        self.labelOutOfServiceTo20_kNm2.setGeometry(QtCore.QRect(310, 120, 51, 21))
        self.labelOutOfServiceTo20_kNm2.setObjectName(_fromUtf8("labelOutOfServiceTo20_kNm2"))
        self.labelOutOfServicePressure = QtGui.QLabel(self.groupBoxOutOfService)
        self.labelOutOfServicePressure.setGeometry(QtCore.QRect(250, 30, 241, 21))
        self.labelOutOfServicePressure.setObjectName(_fromUtf8("labelOutOfServicePressure"))
        self.labelOutOfServiceRatio = QtGui.QLabel(self.groupBoxOutOfService)
        self.labelOutOfServiceRatio.setGeometry(QtCore.QRect(520, 30, 61, 21))
        self.labelOutOfServiceRatio.setObjectName(_fromUtf8("labelOutOfServiceRatio"))
        self.lineEditOutOfServiceRatioTo20 = QtGui.QLineEdit(self.groupBoxOutOfService)
        self.lineEditOutOfServiceRatioTo20.setEnabled(False)
        self.lineEditOutOfServiceRatioTo20.setGeometry(QtCore.QRect(520, 120, 61, 20))
        self.lineEditOutOfServiceRatioTo20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditOutOfServiceRatioTo20.setObjectName(_fromUtf8("lineEditOutOfServiceRatioTo20"))
        self.lineEditOutOfServicePressureTo20 = QtGui.QLineEdit(self.groupBoxOutOfService)
        self.lineEditOutOfServicePressureTo20.setEnabled(False)
        self.lineEditOutOfServicePressureTo20.setGeometry(QtCore.QRect(250, 120, 51, 20))
        self.lineEditOutOfServicePressureTo20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditOutOfServicePressureTo20.setObjectName(_fromUtf8("lineEditOutOfServicePressureTo20"))
        self.lineEditOutOfServiceRatioTo100 = QtGui.QLineEdit(self.groupBoxOutOfService)
        self.lineEditOutOfServiceRatioTo100.setEnabled(False)
        self.lineEditOutOfServiceRatioTo100.setGeometry(QtCore.QRect(520, 190, 61, 20))
        self.lineEditOutOfServiceRatioTo100.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditOutOfServiceRatioTo100.setObjectName(_fromUtf8("lineEditOutOfServiceRatioTo100"))
        self.lineEditOutOfServicePressureTo100 = QtGui.QLineEdit(self.groupBoxOutOfService)
        self.lineEditOutOfServicePressureTo100.setEnabled(False)
        self.lineEditOutOfServicePressureTo100.setGeometry(QtCore.QRect(250, 190, 51, 20))
        self.lineEditOutOfServicePressureTo100.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditOutOfServicePressureTo100.setObjectName(_fromUtf8("lineEditOutOfServicePressureTo100"))
        self.labelOutOfServiceTo100_kNm2 = QtGui.QLabel(self.groupBoxOutOfService)
        self.labelOutOfServiceTo100_kNm2.setGeometry(QtCore.QRect(310, 190, 51, 21))
        self.labelOutOfServiceTo100_kNm2.setObjectName(_fromUtf8("labelOutOfServiceTo100_kNm2"))
        self.lineEditOutOfServiceRatioMore100 = QtGui.QLineEdit(self.groupBoxOutOfService)
        self.lineEditOutOfServiceRatioMore100.setEnabled(False)
        self.lineEditOutOfServiceRatioMore100.setGeometry(QtCore.QRect(520, 260, 61, 20))
        self.lineEditOutOfServiceRatioMore100.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditOutOfServiceRatioMore100.setObjectName(_fromUtf8("lineEditOutOfServiceRatioMore100"))
        self.lineEditOutOfServicePressureMore100 = QtGui.QLineEdit(self.groupBoxOutOfService)
        self.lineEditOutOfServicePressureMore100.setEnabled(False)
        self.lineEditOutOfServicePressureMore100.setGeometry(QtCore.QRect(250, 260, 51, 20))
        self.lineEditOutOfServicePressureMore100.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditOutOfServicePressureMore100.setObjectName(_fromUtf8("lineEditOutOfServicePressureMore100"))
        self.labelOutOfServiceMore100_kNm2 = QtGui.QLabel(self.groupBoxOutOfService)
        self.labelOutOfServiceMore100_kNm2.setGeometry(QtCore.QRect(310, 260, 51, 21))
        self.labelOutOfServiceMore100_kNm2.setObjectName(_fromUtf8("labelOutOfServiceMore100_kNm2"))
        self.labelOutOfServiceSpeedTo20 = QtGui.QLabel(self.groupBoxOutOfService)
        self.labelOutOfServiceSpeedTo20.setGeometry(QtCore.QRect(20, 90, 181, 21))
        self.labelOutOfServiceSpeedTo20.setObjectName(_fromUtf8("labelOutOfServiceSpeedTo20"))
        self.labelOutOfServiceSpeedTo100 = QtGui.QLabel(self.groupBoxOutOfService)
        self.labelOutOfServiceSpeedTo100.setGeometry(QtCore.QRect(20, 160, 181, 21))
        self.labelOutOfServiceSpeedTo100.setObjectName(_fromUtf8("labelOutOfServiceSpeedTo100"))
        self.labelOutOfServiceSpeedMore100 = QtGui.QLabel(self.groupBoxOutOfService)
        self.labelOutOfServiceSpeedMore100.setGeometry(QtCore.QRect(20, 230, 181, 21))
        self.labelOutOfServiceSpeedMore100.setObjectName(_fromUtf8("labelOutOfServiceSpeedMore100"))
        self.groupBoxTravelling = QtGui.QGroupBox(Dialog)
        self.groupBoxTravelling.setEnabled(True)
        self.groupBoxTravelling.setGeometry(QtCore.QRect(340, 180, 601, 101))
        self.groupBoxTravelling.setObjectName(_fromUtf8("groupBoxTravelling"))
        self.labelTravellingSpeed = QtGui.QLabel(self.groupBoxTravelling)
        self.labelTravellingSpeed.setGeometry(QtCore.QRect(20, 30, 181, 21))
        self.labelTravellingSpeed.setObjectName(_fromUtf8("labelTravellingSpeed"))
        self.lineEditTravellingSpeed_ms = QtGui.QLineEdit(self.groupBoxTravelling)
        self.lineEditTravellingSpeed_ms.setGeometry(QtCore.QRect(20, 60, 51, 21))
        self.lineEditTravellingSpeed_ms.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditTravellingSpeed_ms.setObjectName(_fromUtf8("lineEditTravellingSpeed_ms"))
        self.labelTravelling_ms = QtGui.QLabel(self.groupBoxTravelling)
        self.labelTravelling_ms.setGeometry(QtCore.QRect(80, 60, 31, 21))
        self.labelTravelling_ms.setObjectName(_fromUtf8("labelTravelling_ms"))
        self.labelTravelling_kmh = QtGui.QLabel(self.groupBoxTravelling)
        self.labelTravelling_kmh.setGeometry(QtCore.QRect(180, 60, 41, 21))
        self.labelTravelling_kmh.setObjectName(_fromUtf8("labelTravelling_kmh"))
        self.lineEditTravellingSpeed_kmh = QtGui.QLineEdit(self.groupBoxTravelling)
        self.lineEditTravellingSpeed_kmh.setGeometry(QtCore.QRect(120, 60, 51, 20))
        self.lineEditTravellingSpeed_kmh.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditTravellingSpeed_kmh.setObjectName(_fromUtf8("lineEditTravellingSpeed_kmh"))
        self.labelTravellingPressure = QtGui.QLabel(self.groupBoxTravelling)
        self.labelTravellingPressure.setGeometry(QtCore.QRect(250, 30, 241, 21))
        self.labelTravellingPressure.setObjectName(_fromUtf8("labelTravellingPressure"))
        self.labelTravelling_kNm2 = QtGui.QLabel(self.groupBoxTravelling)
        self.labelTravelling_kNm2.setGeometry(QtCore.QRect(310, 60, 51, 21))
        self.labelTravelling_kNm2.setObjectName(_fromUtf8("labelTravelling_kNm2"))
        self.lineEditTravellingPressure = QtGui.QLineEdit(self.groupBoxTravelling)
        self.lineEditTravellingPressure.setEnabled(False)
        self.lineEditTravellingPressure.setGeometry(QtCore.QRect(250, 60, 51, 20))
        self.lineEditTravellingPressure.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditTravellingPressure.setObjectName(_fromUtf8("lineEditTravellingPressure"))
        self.lineEditTravellingRatio = QtGui.QLineEdit(self.groupBoxTravelling)
        self.lineEditTravellingRatio.setEnabled(False)
        self.lineEditTravellingRatio.setGeometry(QtCore.QRect(520, 60, 61, 20))
        self.lineEditTravellingRatio.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEditTravellingRatio.setObjectName(_fromUtf8("lineEditTravellingRatio"))
        self.labelTravellingRatio = QtGui.QLabel(self.groupBoxTravelling)
        self.labelTravellingRatio.setGeometry(QtCore.QRect(520, 30, 61, 21))
        self.labelTravellingRatio.setObjectName(_fromUtf8("labelTravellingRatio"))
        self.groupBoxProject = QtGui.QGroupBox(Dialog)
        self.groupBoxProject.setEnabled(True)
        self.groupBoxProject.setGeometry(QtCore.QRect(20, 60, 301, 391))
        self.groupBoxProject.setObjectName(_fromUtf8("groupBoxProject"))
        self.labelProject = QtGui.QLabel(self.groupBoxProject)
        self.labelProject.setGeometry(QtCore.QRect(22, 30, 181, 21))
        self.labelProject.setObjectName(_fromUtf8("labelProject"))
        self.lineEditProject = QtGui.QLineEdit(self.groupBoxProject)
        self.lineEditProject.setGeometry(QtCore.QRect(20, 60, 261, 20))
        self.lineEditProject.setObjectName(_fromUtf8("lineEditProject"))
        self.labelName = QtGui.QLabel(self.groupBoxProject)
        self.labelName.setGeometry(QtCore.QRect(22, 90, 181, 21))
        self.labelName.setObjectName(_fromUtf8("labelName"))
        self.lineEditName = QtGui.QLineEdit(self.groupBoxProject)
        self.lineEditName.setGeometry(QtCore.QRect(20, 120, 261, 20))
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.labelCompany = QtGui.QLabel(self.groupBoxProject)
        self.labelCompany.setGeometry(QtCore.QRect(22, 150, 181, 21))
        self.labelCompany.setObjectName(_fromUtf8("labelCompany"))
        self.lineEditCompany = QtGui.QLineEdit(self.groupBoxProject)
        self.lineEditCompany.setGeometry(QtCore.QRect(20, 180, 261, 20))
        self.lineEditCompany.setObjectName(_fromUtf8("lineEditCompany"))
        self.labelAuthor = QtGui.QLabel(self.groupBoxProject)
        self.labelAuthor.setGeometry(QtCore.QRect(22, 210, 181, 21))
        self.labelAuthor.setObjectName(_fromUtf8("labelAuthor"))
        self.lineEditAuthor = QtGui.QLineEdit(self.groupBoxProject)
        self.lineEditAuthor.setGeometry(QtCore.QRect(20, 240, 261, 20))
        self.lineEditAuthor.setObjectName(_fromUtf8("lineEditAuthor"))
        self.labelComentary = QtGui.QLabel(self.groupBoxProject)
        self.labelComentary.setGeometry(QtCore.QRect(20, 270, 181, 21))
        self.labelComentary.setObjectName(_fromUtf8("labelComentary"))
        self.textEditComentary = QtGui.QTextEdit(self.groupBoxProject)
        self.textEditComentary.setGeometry(QtCore.QRect(20, 300, 261, 71))
        self.textEditComentary.setObjectName(_fromUtf8("textEditComentary"))
        self.pushButtonOpenProject = QtGui.QPushButton(Dialog)
        self.pushButtonOpenProject.setGeometry(QtCore.QRect(20, 460, 301, 23))
        self.pushButtonOpenProject.setObjectName(_fromUtf8("pushButtonOpenProject"))
        self.pushButtonSaveProject = QtGui.QPushButton(Dialog)
        self.pushButtonSaveProject.setGeometry(QtCore.QRect(20, 500, 301, 23))
        self.pushButtonSaveProject.setObjectName(_fromUtf8("pushButtonSaveProject"))
        self.pushButtonExportDocx = QtGui.QPushButton(Dialog)
        self.pushButtonExportDocx.setGeometry(QtCore.QRect(20, 540, 301, 23))
        self.pushButtonExportDocx.setObjectName(_fromUtf8("pushButtonExportDocx"))
        self.pushButtonExportXlsx = QtGui.QPushButton(Dialog)
        self.pushButtonExportXlsx.setGeometry(QtCore.QRect(20, 580, 301, 23))
        self.pushButtonExportXlsx.setObjectName(_fromUtf8("pushButtonExportXlsx"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEditProject, self.lineEditName)
        Dialog.setTabOrder(self.lineEditName, self.lineEditCompany)
        Dialog.setTabOrder(self.lineEditCompany, self.lineEditAuthor)
        Dialog.setTabOrder(self.lineEditAuthor, self.textEditComentary)
        Dialog.setTabOrder(self.textEditComentary, self.lineEditInServiceSpeed_ms)
        Dialog.setTabOrder(self.lineEditInServiceSpeed_ms, self.lineEditTravellingSpeed_ms)
        Dialog.setTabOrder(self.lineEditTravellingSpeed_ms, self.lineEditOutOfServiceSpeedTo20_ms)
        Dialog.setTabOrder(self.lineEditOutOfServiceSpeedTo20_ms, self.lineEditOutOfServiceSpeedTo100_ms)
        Dialog.setTabOrder(self.lineEditOutOfServiceSpeedTo100_ms, self.lineEditOutOfServiceSpeedMore100_ms)
        Dialog.setTabOrder(self.lineEditOutOfServiceSpeedMore100_ms, self.lineEditInServiceSpeed_kmh)
        Dialog.setTabOrder(self.lineEditInServiceSpeed_kmh, self.lineEditTravellingSpeed_kmh)
        Dialog.setTabOrder(self.lineEditTravellingSpeed_kmh, self.lineEditOutOfServiceSpeedTo20_kmh)
        Dialog.setTabOrder(self.lineEditOutOfServiceSpeedTo20_kmh, self.lineEditOutOfServiceSpeedTo100_kmh)
        Dialog.setTabOrder(self.lineEditOutOfServiceSpeedTo100_kmh, self.lineEditOutOfServiceSpeedMore100_kmh)
        Dialog.setTabOrder(self.lineEditOutOfServiceSpeedMore100_kmh, self.lineEditInServicePressure)
        Dialog.setTabOrder(self.lineEditInServicePressure, self.lineEditTravellingPressure)
        Dialog.setTabOrder(self.lineEditTravellingPressure, self.lineEditOutOfServicePressureTo20)
        Dialog.setTabOrder(self.lineEditOutOfServicePressureTo20, self.lineEditOutOfServicePressureTo100)
        Dialog.setTabOrder(self.lineEditOutOfServicePressureTo100, self.lineEditOutOfServicePressureMore100)
        Dialog.setTabOrder(self.lineEditOutOfServicePressureMore100, self.lineEditInServiceRatio)
        Dialog.setTabOrder(self.lineEditInServiceRatio, self.lineEditTravellingRatio)
        Dialog.setTabOrder(self.lineEditTravellingRatio, self.lineEditOutOfServiceRatioTo20)
        Dialog.setTabOrder(self.lineEditOutOfServiceRatioTo20, self.lineEditOutOfServiceRatioTo100)
        Dialog.setTabOrder(self.lineEditOutOfServiceRatioTo100, self.lineEditOutOfServiceRatioMore100)
        Dialog.setTabOrder(self.lineEditOutOfServiceRatioMore100, self.pushButtonOpenProject)
        Dialog.setTabOrder(self.pushButtonOpenProject, self.pushButtonSaveProject)
        Dialog.setTabOrder(self.pushButtonSaveProject, self.pushButtonExportDocx)
        Dialog.setTabOrder(self.pushButtonExportDocx, self.pushButtonExportXlsx)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Cierzo 0.0.170808", None))
        self.labelTitulo.setText(_translate("Dialog", "Wind action according to FEM 2131/2132", None))
        self.groupBoxInService.setTitle(_translate("Dialog", "Wind action in service (2-2.2.1)", None))
        self.labelInServiceSpeed.setText(_translate("Dialog", "Design wind speed:", None))
        self.lineEditInServiceSpeed_ms.setText(_translate("Dialog", "20", None))
        self.labelInService_ms.setText(_translate("Dialog", "m/s", None))
        self.labelInService_kmh.setText(_translate("Dialog", "km/h", None))
        self.lineEditInServiceSpeed_kmh.setText(_translate("Dialog", "72", None))
        self.labelInServicePressure.setText(_translate("Dialog", "Aerodynamic wind pressure:", None))
        self.labelInService_kNm2.setText(_translate("Dialog", "kN/m²", None))
        self.lineEditInServicePressure.setText(_translate("Dialog", "0,25", None))
        self.lineEditInServiceRatio.setText(_translate("Dialog", "1,000", None))
        self.labelInServiceRatio.setText(_translate("Dialog", "Ratio:", None))
        self.groupBoxOutOfService.setTitle(_translate("Dialog", "Wind action out of service (2-2.3.6)", None))
        self.labelHeight.setText(_translate("Dialog", "Height above sourronding level", None))
        self.labelOutOfServiceSpeed.setText(_translate("Dialog", "Design wind speed:", None))
        self.labelOutOfServiceTo20_kmh.setText(_translate("Dialog", "km/h", None))
        self.labelOutOfServiceTo20_ms.setText(_translate("Dialog", "m/s", None))
        self.lineEditOutOfServiceSpeedTo20_kmh.setText(_translate("Dialog", "129", None))
        self.lineEditOutOfServiceSpeedTo20_ms.setText(_translate("Dialog", "36", None))
        self.lineEditOutOfServiceSpeedTo100_ms.setText(_translate("Dialog", "42", None))
        self.lineEditOutOfServiceSpeedTo100_kmh.setText(_translate("Dialog", "151", None))
        self.labelOutOfServiceTo100_ms.setText(_translate("Dialog", "m/s", None))
        self.labelOutOfServiceTo100_kmh.setText(_translate("Dialog", "km/h", None))
        self.lineEditOutOfServiceSpeedMore100_ms.setText(_translate("Dialog", "46", None))
        self.lineEditOutOfServiceSpeedMore100_kmh.setText(_translate("Dialog", "165", None))
        self.labelOutOfServiceMore100_ms.setText(_translate("Dialog", "m/s", None))
        self.labelOutOfServiceMore100_kmh.setText(_translate("Dialog", "km/h", None))
        self.labelOutOfServiceTo20_kNm2.setText(_translate("Dialog", "kN/m²", None))
        self.labelOutOfServicePressure.setText(_translate("Dialog", "Aerodynamic wind pressure:", None))
        self.labelOutOfServiceRatio.setText(_translate("Dialog", "Ratio:", None))
        self.lineEditOutOfServiceRatioTo20.setText(_translate("Dialog", "3,240", None))
        self.lineEditOutOfServicePressureTo20.setText(_translate("Dialog", "0,79", None))
        self.lineEditOutOfServiceRatioTo100.setText(_translate("Dialog", "4,410", None))
        self.lineEditOutOfServicePressureTo100.setText(_translate("Dialog", "1,08", None))
        self.labelOutOfServiceTo100_kNm2.setText(_translate("Dialog", "kN/m²", None))
        self.lineEditOutOfServiceRatioMore100.setText(_translate("Dialog", "5,290", None))
        self.lineEditOutOfServicePressureMore100.setText(_translate("Dialog", "1,30", None))
        self.labelOutOfServiceMore100_kNm2.setText(_translate("Dialog", "kN/m²", None))
        self.labelOutOfServiceSpeedTo20.setText(_translate("Dialog", "0 to 20 m", None))
        self.labelOutOfServiceSpeedTo100.setText(_translate("Dialog", "20 to 100 m", None))
        self.labelOutOfServiceSpeedMore100.setText(_translate("Dialog", "more than 100 m", None))
        self.groupBoxTravelling.setTitle(_translate("Dialog", "Wind action travelling to storm anchoring (project specification)", None))
        self.labelTravellingSpeed.setText(_translate("Dialog", "Design wind speed:", None))
        self.lineEditTravellingSpeed_ms.setText(_translate("Dialog", "28", None))
        self.labelTravelling_ms.setText(_translate("Dialog", "m/s", None))
        self.labelTravelling_kmh.setText(_translate("Dialog", "km/h", None))
        self.lineEditTravellingSpeed_kmh.setText(_translate("Dialog", "100", None))
        self.labelTravellingPressure.setText(_translate("Dialog", "Aerodynamic wind pressure:", None))
        self.labelTravelling_kNm2.setText(_translate("Dialog", "kN/m²", None))
        self.lineEditTravellingPressure.setText(_translate("Dialog", "0,48", None))
        self.lineEditTravellingRatio.setText(_translate("Dialog", "1,960", None))
        self.labelTravellingRatio.setText(_translate("Dialog", "Ratio:", None))
        self.groupBoxProject.setTitle(_translate("Dialog", "Project", None))
        self.labelProject.setText(_translate("Dialog", "Project:", None))
        self.lineEditProject.setText(_translate("Dialog", "12345 Project", None))
        self.labelName.setText(_translate("Dialog", "Name:", None))
        self.lineEditName.setText(_translate("Dialog", "Structure", None))
        self.labelCompany.setText(_translate("Dialog", "Company:", None))
        self.lineEditCompany.setText(_translate("Dialog", "SPECTRE", None))
        self.labelAuthor.setText(_translate("Dialog", "Author:", None))
        self.lineEditAuthor.setText(_translate("Dialog", "Dr No", None))
        self.labelComentary.setText(_translate("Dialog", "Comentary:", None))
        self.textEditComentary.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'consolas\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">No comment.</span></p></body></html>", None))
        self.pushButtonOpenProject.setText(_translate("Dialog", "Open project...", None))
        self.pushButtonSaveProject.setText(_translate("Dialog", "Save project...", None))
        self.pushButtonExportDocx.setText(_translate("Dialog", "Export to .docx...", None))
        self.pushButtonExportXlsx.setText(_translate("Dialog", "Export to .xlsx...", None))

