# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creditos.ui'
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
        MainWindow.resize(614, 353)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/new_upchiapas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 351, 271))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Semibold"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 20, 151, 141))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.calendarWidget = QtGui.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(340, 170, 271, 141))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 614, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Universidad Politécnica de Chiapas</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Ingeniería en Desarrollo de Software</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Exposicion de programa visual</span></p><p align=\"center\">Programacion Visual</p><p align=\"center\">Catedrático: Juan Carlos López Pimentel</p><p align=\"center\"><span style=\" font-weight:400; text-decoration: underline;\">Integrantes:</span></p><p align=\"center\"><span style=\" font-style:italic;\">Cruz Albores Elihu Alejandro</span></p><p align=\"center\"><span style=\" font-style:italic;\">Farelo Toledo Luis Ángel</span></p><p align=\"center\"><span style=\" font-style:italic;\">Ortíz Escobar Carlos Maximiliano</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/new_upchiapas.png\"/></p></body></html>", None))

##import image_size_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

