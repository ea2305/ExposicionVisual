# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'perdedor.ui'
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

class Ui_Lose(object):
    def setupUi(self, Lose):
        Lose.setObjectName(_fromUtf8("Lose"))
        Lose.setWindowModality(QtCore.Qt.NonModal)
        Lose.resize(386, 146)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(28)
        Lose.setFont(font)
        self.label = QtGui.QLabel(Lose)
        self.label.setGeometry(QtCore.QRect(90, 40, 211, 71))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Lose)
        QtCore.QMetaObject.connectSlotsByName(Lose)

    def retranslateUi(self, Lose):
        Lose.setWindowTitle(_translate("Lose", "You´re loser", None))
        self.label.setText(_translate("Lose", "Ha perdido", None))

