# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newCredits.ui'
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
        Dialog.resize(647, 342)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, 30, 351, 271))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Semibold"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(420, 20, 151, 141))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.calendarWidget = QtGui.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(350, 170, 271, 141))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Universidad Politécnica de Chiapas</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Ingeniería en Desarrollo de Software</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Exposicion de programa visual</span></p><p align=\"center\">Programacion Visual</p><p align=\"center\">Catedrático: Juan Carlos López Pimentel</p><p align=\"center\"><span style=\" font-weight:400; text-decoration: underline;\">Integrantes:</span></p><p align=\"center\"><span style=\" font-style:italic;\">Cruz Albores Elihu Alejandro</span></p><p align=\"center\"><span style=\" font-style:italic;\">Farelo Toledo Luis Ángel</span></p><p align=\"center\"><span style=\" font-style:italic;\">Ortíz Escobar Carlos Maximiliano</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/new_upchiapas.png\"/></p></body></html>", None))

#import image_size_rc
