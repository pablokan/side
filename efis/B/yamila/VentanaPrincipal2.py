from tkinter import CENTER
from turtle import back
from PySide6.QtWidgets import QApplication,QHBoxLayout, QGridLayout,QFrame, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from styles import Text, Input, Button

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 360)
        self.setStyleSheet("background-color: #654321")
        frame1 = QFrame(self)
        frame1.setStyleSheet("background-color: #4CBB7F")
        frame1.setGeometry(0, 0, 500, 200)
        layout1 = QVBoxLayout()
        self.texto = Text('Indumentaria Giro',fontF= "Agency FB", fontS= 40, backg= "#FD4D72", border=2 ,foreg="#4CBB7F",radius=10)
        layout1.addWidget(self.texto)
        boton1 = Button("Resumen semanal de ingresos", backg="White",radius=10,border=1)
        layout1.addWidget(boton1)
        boton1.clicked.connect(self.ResumenSemanal)
        boton2 = Button("Administrador de stock", backg="White",radius=10,border=1)
        layout1.addWidget(boton2)
        boton2.clicked.connect(self.AdministradorStock)
        self.texto2 = Text('Nueva Prenda',radius=10,hAlign="aR",backg="#4CBB7F",foreg="#FD4D72",border=1)
        ancho = self.texto2.sizeHint().width()
        self.texto2.setFixedWidth(ancho)
        layout1.addWidget(self.texto2, alignment=Qt.AlignCenter)
        frame1.setLayout(layout1)

        frame2 = QFrame(self)
        frame2.setStyleSheet("background-color: #4CBB7F")
        frame2.setGeometry(0, 200, 500, 50)
        lay2 = QHBoxLayout()
        text1 = Text("Prenda",border=1,radius=10)
        text2 = Text("Descripcion",border=1,radius=10)
        text3 = Text("Costo",border=1,radius=10)
        textos=[text1,text2,text3]
        for texto in textos:
            lay2.addWidget(texto)
        frame2.setLayout(lay2)

        frame3 = QFrame(self)
        frame3.setStyleSheet("background-color: #4CBB7F")
        frame3.setGeometry(0, 250, 500, 50)
        lay3 = QHBoxLayout()
        cajaText1= Input(backg="White",border=1,radius=10)
        cajaText2= Input(backg="White",border=1,radius=10)
        cajaText3= Input(backg="White",border=1,radius=10)
        cajas=[cajaText1,cajaText2,cajaText3]
        for CajaTexto in cajas:
            lay3.addWidget(CajaTexto)
        frame3.setLayout(lay3)

        frame4=QFrame(self)
        frame4.setStyleSheet("background-color: #4CBB7F")
        frame4.setGeometry(0,300,500,60)
        lay4=QVBoxLayout()
        botonprenda = Button("AGREGAR PRENDA", backg="White",border=1,radius=10)
        lay4.addWidget(botonprenda)
        botonprenda.clicked.connect(self.AgregarPrenda)
        frame4.setLayout(lay4)
        
    def ResumenSemanal(self):
        pass

    def AdministradorStock(self):
        pass

    def AgregarPrenda(self):
        pass

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()