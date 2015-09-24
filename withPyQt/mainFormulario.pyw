import sys

from withPyQt.nuevoFormulario import *


class mainFormulario(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButtonclicker,QtCore.SIGNAL('clicked()'),self.mostrarMensaje)

    def mostrarMensaje(self):
        self.ui.labelMensaje.setText("Hola " + self.ui.lineNombreUsuario.text())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = mainFormulario()
    myapp.show()
    sys.exit(app.exec_())
