from withPyQt.LimpiarCampo import *

class Formulario(QtGui.QMainWindow,Ui_myContainer):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_myContainer()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Formulario()
    myapp.show()
    sys.exit(app.exec_())
