# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\YAIR\OneDrive\Escritorio\Exposición Python\GUI\interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(626, 379)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(244, 220, 199);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbTitulo = QtWidgets.QLabel(self.centralwidget)
        self.lbTitulo.setGeometry(QtCore.QRect(30, 70, 681, 81))
        self.lbTitulo.setStyleSheet("font: 57 22pt \"Engravers MT\";\n"
"\n"
"color: rgb(179, 173, 86);")
        self.lbTitulo.setObjectName("lbTitulo")
        self.lbLado1 = QtWidgets.QLabel(self.centralwidget)
        self.lbLado1.setGeometry(QtCore.QRect(70, 150, 91, 21))
        self.lbLado1.setStyleSheet("font: 75 14pt \"Script MT Bold\";")
        self.lbLado1.setObjectName("lbLado1")
        self.txtLado1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLado1.setGeometry(QtCore.QRect(30, 190, 151, 41))
        self.txtLado1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.txtLado1.setAlignment(QtCore.Qt.AlignCenter)
        self.txtLado1.setObjectName("txtLado1")
        self.lbLado2 = QtWidgets.QLabel(self.centralwidget)
        self.lbLado2.setGeometry(QtCore.QRect(280, 150, 91, 21))
        self.lbLado2.setStyleSheet("font: 75 14pt \"Script MT Bold\";")
        self.lbLado2.setObjectName("lbLado2")
        self.lbLado3 = QtWidgets.QLabel(self.centralwidget)
        self.lbLado3.setGeometry(QtCore.QRect(470, 150, 91, 21))
        self.lbLado3.setStyleSheet("font: 75 14pt \"Script MT Bold\";")
        self.lbLado3.setObjectName("lbLado3")
        self.btnLimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpiar.setGeometry(QtCore.QRect(20, 290, 201, 31))
        self.btnLimpiar.setStyleSheet("font: 8pt \"Lucida Calligraphy\";\n"
"background-color: rgb(255, 144, 89);\n"
"")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.btnAyuda = QtWidgets.QPushButton(self.centralwidget)
        self.btnAyuda.setGeometry(QtCore.QRect(450, 290, 151, 31))
        self.btnAyuda.setStyleSheet("font: 8pt \"Lucida Calligraphy\";\n"
"background-color: rgb(255, 144, 89);\n"
"")
        self.btnAyuda.setObjectName("btnAyuda")
        self.btnTipo = QtWidgets.QPushButton(self.centralwidget)
        self.btnTipo.setGeometry(QtCore.QRect(250, 290, 171, 31))
        self.btnTipo.setStyleSheet("font: 8pt \"Lucida Calligraphy\";\n"
"background-color: rgb(170, 170, 127);")
        self.btnTipo.setObjectName("btnTipo")
        self.lbImg = QtWidgets.QLabel(self.centralwidget)
        self.lbImg.setGeometry(QtCore.QRect(0, 0, 851, 81))
        self.lbImg.setText("")
        self.lbImg.setPixmap(QtGui.QPixmap("c:\\Users\\YAIR\\OneDrive\\Escritorio\\Exposición Python\\GUI\\img.jpg"))
        self.lbImg.setObjectName("lbImg")
        self.txtLado2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLado2.setGeometry(QtCore.QRect(250, 190, 151, 41))
        self.txtLado2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.txtLado2.setAlignment(QtCore.Qt.AlignCenter)
        self.txtLado2.setObjectName("txtLado2")
        self.txtLado3 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLado3.setGeometry(QtCore.QRect(450, 190, 151, 41))
        self.txtLado3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.txtLado3.setAlignment(QtCore.Qt.AlignCenter)
        self.txtLado3.setObjectName("txtLado3")
        self.lbResultado = QtWidgets.QLabel(self.centralwidget)
        self.lbResultado.setGeometry(QtCore.QRect(170, 250, 341, 20))
        self.lbResultado.setStyleSheet("font: 9pt \"Yu Gothic\";")
        self.lbResultado.setObjectName("lbResultado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 626, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbTitulo.setText(_translate("MainWindow", "TIPOS DE TRIÁNGULOS"))
        self.lbLado1.setText(_translate("MainWindow", "LADO 1:"))
        self.lbLado2.setText(_translate("MainWindow", "LADO 2:"))
        self.lbLado3.setText(_translate("MainWindow", "LADO 3:"))
        self.btnLimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.btnAyuda.setText(_translate("MainWindow", "AYUDA"))
        self.btnTipo.setText(_translate("MainWindow", "DETERMINAR TIPO"))
        self.lbResultado.setText(_translate("MainWindow", "> TIPO DE TRIÁNGULO: Desconocido"))