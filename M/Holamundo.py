# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'holamundo.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(414, 420)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lbl_holamundovisual = QtGui.QLabel(self.centralwidget)
        self.lbl_holamundovisual.setGeometry(QtCore.QRect(180, 270, 61, 31))
        self.lbl_holamundovisual.setObjectName(_fromUtf8("lbl_holamundovisual"))
        self.btn_clic = QtGui.QPushButton(self.centralwidget)
        self.btn_clic.setGeometry(QtCore.QRect(170, 310, 75, 23))
        self.btn_clic.setObjectName(_fromUtf8("btn_clic"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 0, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 414, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btn_clic, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lbl_holamundovisual.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lbl_holamundovisual.setText(_translate("MainWindow", "Hola mundo", None))
        self.btn_clic.setText(_translate("MainWindow", "Clic me", None))
        self.pushButton.setText(_translate("MainWindow", "Hola mundo", None))

