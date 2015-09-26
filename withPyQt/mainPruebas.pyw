__author__ = 'Elihu Alejandro, Max Escobar, Luis Toledo'
#Menu Principal para despliegue del programa
#version 1.5

import sys#importamos funcionalidades de sys
import random
from withPyQt.ventanaCreditos import *#importamos nuestra ventana de menu de creditos
from withPyQt.newCredits import *#importamos la ventana de creditos
from withPyQt.AreYouSure import *
from withPyQt.perdedor import *

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

#Clase que emerge ventada para indicar que el usuario perdio

class perdio(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Lose()
        self.ui.setupUi(self)

class areYouSure(QtGui.QDialog):

    bufferNick = 'none'

    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.btnYes,QtCore.SIGNAL('clicked()'),self.asignarNickname)
        QtCore.QObject.connect(self.ui.btnYes,QtCore.SIGNAL('clicked()'),self.Close)

    def asignarNickname(self):
        print("hola")
        self.close()

    def Close(self):
        self.close()

#Clase de creditos hereda de Qtgui para obtener funcion exec()
class misCreditos(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

#Clase de main del programa herada de Qtgui para funcion exec()
class mainVentana(QtGui.QDialog):

    state = False
    Nick = "Persona"
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
        QtCore.QObject.connect(self.ui.pushButton_6,QtCore.SIGNAL('clicked()'),self.getNickname)


    def Warning(self):
        Ventana = perdio()
        Ventana.exec_()

    def getNickname(self):
        Buffer = self.ui.lineNickname.text()
        if(Buffer != self.Nick):
            alert = areYouSure()
            alert.exec_()
        else:
            self.Nick = Buffer

    #metodo para visualizar los creditos
    def mostrarVentana(self):
        mycredits = misCreditos()
        mycredits.ui.ThankYou.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-style:italic; text-decoration: underline;\">Game over </span></p><p align=\"center\">Gracias por jugar nuestro juego " + str(self.Nick) + " !!</p></body></html>", None))
        mycredits.exec_()

    #Validacion de entrada opciones
    def JuegoOpcion(self, a):

        OpcionCorrecta = (random.randrange(2) + 1)
        if(a == OpcionCorrecta or a == 3):
            self.Score += 1
            self.ui.label.setText(_translate("DialogCreditos", "<html><head/><body><p><span style=\" font-size:16pt;\">" + str(self.Score) + "</span></p></body></html>", None))
            self.ui.labelMensjae.setText(_translate("DialogCreditos", "<html><head/><body><p><span style=\" font-size:16pt;\">Acierto!!</span></p></body></html>", None))

        else:
            self.Score = 0
            self.ui.labelMensjae.setText("")
            self.ui.label.setText(_translate("DialogCreditos", "<html><head/><body><p><span style=\" font-size:16pt;\">0</span></p></body></html>", None))
            self.ui.labelTitulo.setText(_translate("DialogCreditos", "<html><head/><body><p><span style=\" font-size:16pt;\">Desea iniciar?</span></p></body></html>", None))
            mycredits = misCreditos()
            mycredits.ui.ThankYou.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-style:italic; text-decoration: underline;\">Game over </span></p><p align=\"center\">Gracias por jugar nuestro juego :v " + str(self.Nick) + " !!</p></body></html>", None))
            self.state = False
            self.mostrarVentana()

    #inicio de juego
    def startGame(self):
        self.ui.labelTitulo.setText(_translate("DialogCreditos", "<html><head/><body><p><span style=\" font-size:16pt;\">Running!!</span></p></body></html>", None))
        self.state = True

    #Seleccion de opcion a
    def opcionA(self):
        if (self.state != False):
            self.JuegoOpcion(1)

    #Seleccion de opcion b
    def opcionB(self):
        if (self.state != False):
            self.JuegoOpcion(2)

    #Seleccion de opcion c
    def opcionC(self):
        if (self.state != False):
            self.JuegoOpcion(3)

#Instancia y ejecucion
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = mainVentana()
    myapp.show()
    sys.exit(app.exec_())