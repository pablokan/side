import os, sys
sys.path.append(os.path.abspath('libs'))

from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout, QMessageBox)
from styles import Text, Input, Button

class Window(QWidget):
    def __init__(self, cantidad):
        super().__init__()
        self.layout = layout = QVBoxLayout()
        mensaje = Text("Carga de edades")
        layout.addWidget(mensaje)

        for i in range(cantidad):
            layout.addWidget(Input())
        b = Button("Promediar")
        layout.addWidget(b)
        b.clicked.connect(self.promediar)

        self.setLayout(layout)

    def promediar(self):
        edades = self.findChildren(Input)
        t = 0
        for edad in edades:
            t += int(edad.text())
        salida = Text(f"Promedio: {t//len(edades)}")
        self.layout.addWidget(salida)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.layout = layout = QVBoxLayout()

        self.mensaje = Text('Cuántos datos quiere cargar?', fontS=30)
        layout.addWidget(self.mensaje)
        
        self.entrada = Input('', fontS=30)
        layout.addWidget(self.entrada)
        
        self.boton = boton = Button('Cargar', fontS=30)
        layout.addWidget(boton)
        boton.setDefault(True)
        boton.clicked.connect(self.cargar)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def cargar(self):
        self.w = Window(int(self.entrada.text()))
        self.w.show()
        
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
