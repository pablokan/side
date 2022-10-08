import os, sys
sys.path.append(os.path.abspath('libs'))

from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem, QFormLayout, QHBoxLayout)
from PySide6.QtCore import Qt

from styles import Text, Input, Button


class Table(QTableWidget):
    def __init__(self, data, header):
        super().__init__()
        self.setRowCount(len(data))
        self.setColumnCount(len(data[0]))
        self.setHorizontalHeaderLabels(header)
        for x in range(len(data)):
            for y in range(len(data[x])):
                celda = str(data[x][y])
                if celda.isdigit():
                    celda = int(celda)
                item = QTableWidgetItem(celda)
                item.setData(Qt.DisplayRole, celda) # para que ordene por numeración
                self.setItem(x, y, item)
        self.resizeColumnsToContents()

    def getAll(self) -> list:
        tabla = []
        for f in range (self.rowCount()):
            fila = []
            for c in range(self.columnCount()):
                fila.append(self.item(f, c).text())
            tabla.append(fila)
        return tabla

class MainWindow(QMainWindow):
    def __init__(self, datos, cabeza):
        super().__init__()

        self.empleados = []
        layout = QVBoxLayout()
        formu = QFormLayout()
        formu.addRow("Nombre", Input())
        formu.addRow("Salario", Input())
        layout.addLayout(formu)
        botonera = QHBoxLayout()
        bAdd = Button('Agregar', foreg='red', backg='yellow')
        botonera.addWidget(bAdd)
        bAdd.setDefault(True)
        bAdd.clicked.connect(self.listAdd)
        
        bProcesar = Button('Procesar', foreg='red', backg='yellow')
        botonera.addWidget(bProcesar)
        #bProcesar.setDefault(True)
        bProcesar.clicked.connect(self.procesar)
        layout.addLayout(botonera)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def listAdd(self):
        lista = []
        for e in self.findChildren(Input):
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
    personas = [
        ("Juan", "1990-02-07"),
        ("Luis", "2007-01-25"),
        ("Ana", "2000-12-30")
        ]
    window = MainWindow(personas, ("Nombre", "Fecha de nacimiento"))
    window.show()
    app.exec()
