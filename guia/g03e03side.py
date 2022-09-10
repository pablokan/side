#1: Almacenar en dos listas paralelas, nombres y sexos de 8 personas. 
#2: Recorrerlas y mostrar los nombres de las mujeres. 

from tkinter import mainloop
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QPushButton, QRadioButton, QGridLayout, QButtonGroup)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        
        cuadricula = QGridLayout()

        for x in range (8):
            cuadricula.addWidget(QLineEdit(), x, 0)
            bg = QButtonGroup()
            rbF = QRadioButton("Femenino", self)
            rbF.toggled.connect(self.updateLabel)
            rbM = QRadioButton("Masculino", self)
            rbM.toggled.connect(self.updateLabel)
            cuadricula.addWidget(rbF, x, 1)
            cuadricula.addWidget(rbM, x, 2)
            bg.addButton(rbF)
            bg.addButton(rbM)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(cuadricula)
        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

    def updateLabel(self):
        pass
    
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
