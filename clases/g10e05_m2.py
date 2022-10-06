import os, sys
sys.path.append(os.path.abspath('libs'))

from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout)
from styles import Text, Input, Button

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
        self.mensaje.setText("Carga de edades")
        self.entrada.deleteLater()
        self.boton.close()
        cantidad = int(self.entrada.text())
        for i in range(cantidad):
            self.layout.addWidget(Input())
        b = Button("Promediar")
        self.layout.addWidget(b)
        b.clicked.connect(self.promediar)

    def promediar(self):
        edades = self.findChildren(Input)
        t = 0
        for edad in edades:
            t += int(edad.text())
        salida = Text(f"Promedio: {t//len(edades)}")
        self.layout.addWidget(salida)
        
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
