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
        DialogCreditos.resize(400, 300)
        self.pushButton = QtGui.QPushButton(DialogCreditos)
        self.pushButton.setGeometry(QtCore.QRect(140, 130, 121, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(DialogCreditos)
        QtCore.QMetaObject.connectSlotsByName(DialogCreditos)

    def retranslateUi(self, DialogCreditos):
        DialogCreditos.setWindowTitle(_translate("DialogCreditos", "Dialog", None))
        self.pushButton.setText(_translate("DialogCreditos", "Créditos", None))

