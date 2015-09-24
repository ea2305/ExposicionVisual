#Menu Principal para despliegue del programa
#Authores:
#version 1.2

import sys#importamos funcionalidades de sys
from withPyQt.ventanaCreditos import *#importamos nuestra ventana de menu de creditos
from withPyQt.newCredits import *#importamos la ventana de creditos

#Clase de creditos hereda de Qtgui para obtener funcion exec()
class misCreditos(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

#Clase de main del programa herada de Qtgui para funcion exec()
class mainVentana(QtGui.QDialog):

    #Constructor que no tiene padre para ser el frame principal
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_DialogCreditos()
        self.ui.setupUi(self)

        #Evento de boton, para creditos
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.mostrarVentana)

    #metodo para visualizar los creditos,
    def mostrarVentana(self):
        mycredits = misCreditos().exec()

#Instancia y ejecución
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = mainVentana()
    myapp.show()
    sys.exit(app.exec_())