# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nuevoFormulario.ui'
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
        Dialog.resize(290, 300)
        self.labelEscribirNombre = QtGui.QLabel(Dialog)
        self.labelEscribirNombre.setGeometry(QtCore.QRect(110, 40, 111, 20))
        self.labelEscribirNombre.setObjectName(_fromUtf8("labelEscribirNombre"))
        self.lineNombreUsuario = QtGui.QLineEdit(Dialog)
        self.lineNombreUsuario.setGeometry(QtCore.QRect(40, 90, 113, 20))
        self.lineNombreUsuario.setObjectName(_fromUtf8("lineNombreUsuario"))
        self.pushButtonclicker = QtGui.QPushButton(Dialog)
        self.pushButtonclicker.setGeometry(QtCore.QRect(180, 90, 75, 23))
        self.pushButtonclicker.setObjectName(_fromUtf8("pushButtonclicker"))
        self.labelMensaje = QtGui.QLabel(Dialog)
        self.labelMensaje.setGeometry(QtCore.QRect(140, 140, 46, 13))
        self.labelMensaje.setObjectName(_fromUtf8("labelMensaje"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelEscribirNombre.setText(_translate("Dialog", "Escriba su nombre", None))
        self.pushButtonclicker.setText(_translate("Dialog", "PushButton", None))
        self.labelMensaje.setText(_translate("Dialog", "Waiting...", None))

