import os, sys
sys.path.append(os.path.abspath('libs'))

from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout)
from styles import Text, Input, Button

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.entrada = Input('Input', fontF='Calibri', fontS=20)
        layout.addWidget(self.entrada)
        self.texto = Text('Text', foreg='cyan', backg='#123456', hAlign='aL', border=3, radius=0)
        layout.addWidget(self.texto)
        boton = Button('Button', foreg='red', backg='yellow')
        layout.addWidget(boton)
        boton.setDefault(True)
        boton.clicked.connect(self.functionName)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def functionName(self):
        self.texto.setText(f'Hola {self.entrada.text()}')

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
