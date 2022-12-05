''''import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class ejemplo_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interfaz.ui",self)
if __name__ == '__main__':
    app= QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec_())'''
    
# CODIGO PREDETERMINADO
'''''import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "HolaMundo.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        

if _name_ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())'''
    
'''---------------------PYQT5---------------
instalar la libreria 
pip install pyqt5

intalar las herramientass
pip install pyqt5-tools

Actualizar la version del pip
python –m pip install –U pip'''