import os, sys
sys.path.append(os.path.abspath('libs'))

from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QLabel)
from PySide6.QtGui import QIntValidator

class InputInt(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setValidator(QIntValidator())

class Window(QWidget):
    def __init__(self, cantidad):
        super().__init__()
        self.layout = layout = QVBoxLayout()

        texto = QLabel("Carga de edades")
        layout.addWidget(texto)
        for _ in range(cantidad):
            layout.addWidget(InputInt())
        b = QPushButton("Promediar")
        b.clicked.connect(self.promediar)
        layout.addWidget(b)
        self.setLayout(layout)

    def promediar(self):
        t = 0
        edades = self.findChildren(QLineEdit)
        for edad in edades:
            t += int(edad.text())
        salida = QLabel(f"El promedio es {t//len(edades)}")
        self.layout.addWidget(salida)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.layout = layout = QVBoxLayout()

        self.texto = QLabel('Cuántas edades va a cargar?')
        layout.addWidget(self.texto)

        self.entrada = InputInt()
        layout.addWidget(self.entrada)
        
        self.boton = boton = QPushButton('Cargar')
        layout.addWidget(boton)
        boton.setDefault(True)
        boton.clicked.connect(self.cargar)
        
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def cargar(self):
        cantidad = int(self.entrada.text())
        self.w = Window(cantidad)
        self.w.show()

if __name__ == '__main__':
    app = QApplication()
    css = '*{font-size: 20px; background-color: #5692de; color: #1b1047;}'
    app.setStyleSheet(css)
    window = MainWindow()
    window.show()
    app.exec()
