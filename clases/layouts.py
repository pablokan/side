import os, sys
sys.path.append(os.path.abspath('libs'))
print(sys.path)
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QFormLayout, QHBoxLayout
from styles import Text, Input, Button

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mainLayout = QVBoxLayout()
        formulario = QFormLayout()
        botonera = QHBoxLayout()
        formulario.addRow(Text("Nombre", fore="red"), Input(fore="red"))
        formulario.addRow(Text("Edad", fore="red"), Input(fore="red"))
        bEnter = Button("Enter")
        botonera.addWidget(bEnter)
        bNada = Button("Nada")
        botonera.addWidget(bNada)

        mainLayout.addLayout(formulario) 
        mainLayout.addLayout(botonera)
               
        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
