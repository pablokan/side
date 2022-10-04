import os, sys
sys.path.append(os.path.abspath('libs'))

from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QFormLayout)
from styles import Text, Input, Button

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mainLayout = QVBoxLayout() # Estructura principal
        
        formulario = QFormLayout() # formulario
        formulario.addRow(Text("Nombre", backg="red"), Input(backg="red"))
        formulario.addRow(Text("Edad", backg="red"), Input(backg="red"))
        mainLayout.addLayout(formulario) # add form to mainLayout

        mainLayout.addWidget(Text('cualquier cosa entre el form y los botones', backg="green")) # agrego texto al medio
        
        botonera = QHBoxLayout() # defino estructura inferior
        botonera.addWidget(Button("OK", backg="blue"))
        botonera.addWidget(Button("Cancel", backg="blue"))
        mainLayout.addLayout(botonera) # agrego la botonera a la estructura principal

        # lo que va siempre
        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout) # esta DEBE SER la estructura principal
        self.setCentralWidget(centralWidget)

    
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
