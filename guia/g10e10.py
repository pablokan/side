import os, sys
sys.path.append(os.path.abspath('libs'))

from PySide6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QVBoxLayout, 
    QTableWidget, QTableWidgetItem, QFormLayout, QHBoxLayout,
    QLineEdit, QPushButton,
    )
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.empleados = []
        layout = QVBoxLayout()
        formu = QFormLayout()
        formu.addRow("Nombre", QLineEdit())
        formu.addRow("Salario", QLineEdit())
        layout.addLayout(formu)
        botonera = QHBoxLayout()
        bAdd = QPushButton('Agregar')
        botonera.addWidget(bAdd)
        bAdd.setDefault(True)
        bAdd.clicked.connect(self.listAdd)
        
        bProcesar = QPushButton('Procesar')
        botonera.addWidget(bProcesar)
        #bProcesar.setDefault(True)
        bProcesar.clicked.connect(self.procesar)
        layout.addLayout(botonera)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def listAdd(self):
        lista = []
        for e in self.findChildren(QLineEdit):
            if e.text().isdigit():
                d = int(e.text())
            else:
                d = e.text()
            lista.append(d)

        self.empleados.append(lista)
        print(self.empleados)

    def procesar(self):
        print(min(self.empleados, key=lambda user: user[1]))

if __name__ == '__main__':
    app = QApplication()
    css = '*{font-size: 20px; background-color: #b56576; color: #130218;}'
    app.setStyleSheet(css)    
    window = MainWindow()
    window.show()
    app.exec()
