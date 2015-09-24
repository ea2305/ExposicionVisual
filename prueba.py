 # -*- coding: utf-8 -*-
import sys

from PyQt4 import QtGui, QtCore
from NewLabel import NewLabel

def imprimir():
    print ("CLICK")

def main():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QMainWindow()
    w.resize(400, 200)
    w.move(300, 300)
    w.setWindowTitle('Mi primer widget')

    #Creamos nuestra primer etiqueta
    new_label = NewLabel("Primer etiqueta", w)
    new_label.setStyleSheet("NewLabel {background-color:red;}")

    #Conectamos la señal con el lisener imprimir
    new_label.connect(new_label,QtCore.SIGNAL("clicked()"),imprimir)

    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

