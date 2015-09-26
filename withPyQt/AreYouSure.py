# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AreYouSure.ui'
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
        Dialog.resize(391, 128)
        self.btnYes = QtGui.QPushButton(Dialog)
        self.btnYes.setGeometry(QtCore.QRect(90, 80, 75, 23))
        self.btnYes.setObjectName(_fromUtf8("btnYes"))
        self.btnNo = QtGui.QPushButton(Dialog)
        self.btnNo.setGeometry(QtCore.QRect(220, 80, 75, 23))
        self.btnNo.setObjectName(_fromUtf8("btnNo"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(5, 12, 391, 41))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.btnYes.setText(_translate("Dialog", "Si", None))
        self.btnNo.setText(_translate("Dialog", "No", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#e3aa19;\">¿ Desea modificar el Nickname ? </span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

