# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaCreditos.ui'
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

class Ui_DialogCreditos(object):
    def setupUi(self, DialogCreditos):
        DialogCreditos.setObjectName(_fromUtf8("DialogCreditos"))
        DialogCreditos.resize(390, 300)
        self.pushButton = QtGui.QPushButton(DialogCreditos)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 71, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(DialogCreditos)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 220, 101, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(DialogCreditos)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 220, 101, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(DialogCreditos)
        self.pushButton_4.setGeometry(QtCore.QRect(274, 220, 101, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.labelOpcion1 = QtGui.QLabel(DialogCreditos)
        self.labelOpcion1.setGeometry(QtCore.QRect(20, 150, 111, 20))
        self.labelOpcion1.setObjectName(_fromUtf8("labelOpcion1"))
        self.label_2Opcion2 = QtGui.QLabel(DialogCreditos)
        self.label_2Opcion2.setGeometry(QtCore.QRect(150, 150, 111, 20))
        self.label_2Opcion2.setObjectName(_fromUtf8("label_2Opcion2"))
        self.label_3Opcion3 = QtGui.QLabel(DialogCreditos)
        self.label_3Opcion3.setGeometry(QtCore.QRect(275, 150, 111, 20))
        self.label_3Opcion3.setObjectName(_fromUtf8("label_3Opcion3"))
        self.labelTitulo = QtGui.QLabel(DialogCreditos)
        self.labelTitulo.setGeometry(QtCore.QRect(20, 60, 181, 31))
        self.labelTitulo.setObjectName(_fromUtf8("labelTitulo"))
        self.label = QtGui.QLabel(DialogCreditos)
        self.label.setGeometry(QtCore.QRect(220, 10, 161, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_5 = QtGui.QPushButton(DialogCreditos)
        self.pushButton_5.setGeometry(QtCore.QRect(220, 70, 151, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        self.retranslateUi(DialogCreditos)
        QtCore.QMetaObject.connectSlotsByName(DialogCreditos)

    def retranslateUi(self, DialogCreditos):
        DialogCreditos.setWindowTitle(_translate("DialogCreditos", "Dialog", None))
        self.pushButton.setText(_translate("DialogCreditos", "Créditos", None))
        self.pushButton_2.setText(_translate("DialogCreditos", "Opción A", None))
        self.pushButton_3.setText(_translate("DialogCreditos", "Opción B", None))
        self.pushButton_4.setText(_translate("DialogCreditos", "Opción C", None))
        self.labelOpcion1.setText(_translate("DialogCreditos", "<html><head/><body><p><span style=\" font-weight:600;\">Posición número 1</span></p></body></html>", None))
        self.label_2Opcion2.setText(_translate("DialogCreditos", "<html><head/><body><p><span style=\" font-weight:600;\">Posición número 2</span></p></body></html>", None))
        self.label_3Opcion3.setText(_translate("DialogCreditos", "<html><head/><body><p><span style=\" font-weight:600;\">Posición número 3</span></p></body></html>", None))
        self.labelTitulo.setText(_translate("DialogCreditos", "<html><head/><body><p><span style=\" font-size:16pt;\">Desea iniciar?</span></p></body></html>", None))
        self.label.setText(_translate("DialogCreditos", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">0</span></p></body></html>", None))
        self.pushButton_5.setText(_translate("DialogCreditos", "Start/Restart", None))

