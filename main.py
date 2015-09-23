#Python Team :D
#version 1.1
import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

elemento = QtGui.QWidget()
elemento.resize(640,480)
elemento.setWindowTitle('Hola mundo!')
elemento.show()

sys.exit(app.exec_())