__author__ = 'ElihuAlejandro'
from PyQt4 import QtCore, QtGui

class NewLabel(QtGui.QLabel):
    def __init__(self, firstLabel, parent = None):
        QtGui.QLabel.__init__(self, firstLabel, parent)

    def mousePressEvent(self, event):
        self.emit(QtCore.SIGNAL('clicked()'))