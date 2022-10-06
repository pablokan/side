import os, sys
sys.path.append(os.path.abspath('libs'))

from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout)
from styles import Text, Input, Button


class Window(QMainWindow):
    def __init__(self, c):
        super().__init__()

        layout = QVBoxLayout()
        for x in range(c):
            self.entrada = Input('Input', fontF='Calibri', fontS=20)
            layout.addWidget(self.entrada)
        
        boton = Button('Button', foreg='red', backg='yellow')
        layout.addWidget(boton)
        boton.setDefault(True)
        #boton.clicked.connect(self.functionName)
        
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        texto = Text('Text', foreg='cyan', backg='#123456')
        layout.addWidget(texto)     
        self.cantidad = Input('Input', fontF='Calibri', fontS=20)
        layout.addWidget(self.cantidad)
        boton = Button('Button', foreg='red', backg='yellow')
        layout.addWidget(boton)
        boton.setDefault(True)
        boton.clicked.connect(self.functionName)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def functionName(self):
        self.w = Window(int(self.cantidad.text()))
        self.w.show()

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
