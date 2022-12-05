from triangulo import Triangulo
import sys
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

qtCreatorFile="GUI/interfaz.ui"
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnTipo.clicked.connect(self.calcular)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.setWindowTitle("INTERFAZ")
        self.btnAyuda.clicked.connect(self.ayuda)
        
    def calcular(self):
        if len(self.txtLado1.text())!=0 and len(self.txtLado2.text())!=0 and len(self.txtLado3.text())!=0:
           a = int(self.txtLado1.text())
           b = int(self.txtLado2.text())
           c = int(self.txtLado3.text())
           
           tipo= Triangulo(a,b,c).get_Tipo()
           self.lbResultado.setText("> EL TIPO DE TRIÁNGULO ES : "+ tipo)
        else:
            self.lbResultado.setText(" COMPLETE LOS CAMPOS VACIOS ") 
    
    def limpiar(self):
        self.txtLado1.clear()
        self.txtLado2.clear()
        self.txtLado3.clear()
    
    def ayuda(self):
        QMessageBox.about(self, "Ayuda", "Ingresa los lados y determina el tipo de triángulo")
    
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())