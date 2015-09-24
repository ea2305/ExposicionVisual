# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LimpiarCampo.ui'
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

class Ui_myContainer(object):
    def setupUi(self, myContainer):
        myContainer.setObjectName(_fromUtf8("myContainer"))
        myContainer.resize(219, 182)
        self.centralwidget = QtGui.QWidget(myContainer)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 91, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 50, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 90, 91, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        myContainer.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(myContainer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 219, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        myContainer.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(myContainer)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        myContainer.setStatusBar(self.statusbar)

        self.retranslateUi(myContainer)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(myContainer)

    def retranslateUi(self, myContainer):
        myContainer.setWindowTitle(_translate("myContainer", "MainWindow", None))
        self.label.setText(_translate("myContainer", "Ingrese su nombre", None))
        self.pushButton.setText(_translate("myContainer", "Limpiar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    myContainer = QtGui.QMainWindow()
    ui = Ui_myContainer()
    ui.setupUi(myContainer)
    myContainer.show()
    sys.exit(app.exec_())

