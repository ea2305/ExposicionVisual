#importamos funcionalidades de sys

import sys
from M.Holamundo import *


class holamundo(QtGui.QMainWindow):



    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL('clicked()'),self.mostrarhm)

    def mostrarhm(self):
         self.ui.lbl_holamundovisual.setText("Reapareci :)")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = holamundo()
    myapp.show()
    sys.exit(app.exec_())

