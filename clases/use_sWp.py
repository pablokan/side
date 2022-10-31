import os, sys
sys.path.append(os.path.abspath('libs'))

from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout, QFrame)
from stylesWithPositions import Text, Input, Button

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 700) # tamaño fijo de la ventana (ancho y alto)
        self.setStyleSheet("background-color: yellow;") # color de fondo de la ventana
        frameAzul = QFrame(self)
        frameAzul.setGeometry(10, 10, 500, 400)
        frameAzul.setStyleSheet("background-color: blue;")
    
        frameRojo = QFrame(self)
        frameRojo.setGeometry(200, 200, 400, 400)
        frameRojo.setStyleSheet("background-color: red;")
        
        boton2 = Button("Botón grande", fontS=40, border=5, parent=frameAzul, posAsize=(10,10,400,80))
        boton3 = Button("Botón celeste", backg='#3582db', parent=frameRojo, posAsize=(10,10,200,60))    
        boton2.clicked.connect(self.algo)

    def algo(self):
        print('algo')

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
