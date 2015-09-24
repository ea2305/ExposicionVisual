__author__ = 'Elihu Alejandro, Max Escobar, Luis Toledo'
#Menu Principal para despliegue del programa
#version 1.2

import sys#importamos funcionalidades de sys
import random
from withPyQt.ventanaCreditos import *#importamos nuestra ventana de menu de creditos
from withPyQt.newCredits import *#importamos la ventana de creditos
from withPyQt.perdedor import *


#Clase que emerge ventada para indicar que el usuario perdio

class perdio(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)

#Clase de creditos hereda de Qtgui para obtener funcion exec()
class misCreditos(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

#Clase de main del programa herada de Qtgui para funcion exec()
class mainVentana(QtGui.QDialog):

    state = False
    Score = 0

    #Constructor que no tiene padre para ser el frame principal
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_DialogCreditos()
        self.ui.setupUi(self)

        #Evento de boton, para creditos
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.mostrarVentana)
        QtCore.QObject.connect(self.ui.pushButton_2,QtCore.SIGNAL('clicked()'),self.opcionA)
        QtCore.QObject.connect(self.ui.pushButton_3,QtCore.SIGNAL('clicked()'),self.opcionB)
        QtCore.QObject.connect(self.ui.pushButton_4,QtCore.SIGNAL('clicked()'),self.opcionC)
        QtCore.QObject.connect(self.ui.pushButton_5,QtCore.SIGNAL('clicked()'),self.startGame)

    #metodo para imprimir que perdio
    def mensajeperdio(self):
        vperdio = perdio().exec()
    #metodo para visualizar los creditos
    def mostrarVentana(self):
        mycredits = misCreditos().exec()

    #Validacion de entrada opciones
    def JuegoOpcion(self, a):

        OpcionCorrecta = (random.randrange(2) + 1)
        print(OpcionCorrecta)
        if(a == OpcionCorrecta or a == 3):
            self.Score += 1
            self.ui.label.setText(str(self.Score))
            self.ui.labelMensjae.setText("Acierto!!")
            print("Ok")
        else:
            self.Score = 0
            self.ui.labelMensjae.setText("")
            self.ui.label.setText("0")
            print(" :c")
            self.mensajeperdio()
        pass

    #inicio de juego
    def startGame(self):
        self.ui.labelTitulo.setText("Running!!")
        print(self.state)
        self.state = True
        print(self.state)

    #Seleccion de opcion a
    def opcionA(self):
        a = 1
        print(self.state)
        if (self.state != False):
            self.JuegoOpcion(a)

    #Seleccion de opcion b
    def opcionB(self):
        a = 2
        if (self.state != False):
            self.JuegoOpcion(a)

    #Seleccion de opcion c
    def opcionC(self):
        a = 3
        if (self.state != False):
            self.JuegoOpcion(a)


#Instancia y ejecucion
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = mainVentana()
    myapp.show()
    sys.exit(app.exec_())