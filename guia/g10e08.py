import os, sys
sys.path.append(os.path.abspath('libs'))

from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem)
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

        layout = QVBoxLayout()
        self.t = t = Table(datos, cabeza)
        layout.addWidget(t)
        boton = Button('Button', foreg='red', backg='yellow')
        layout.addWidget(boton)
        boton.setDefault(True)
        boton.clicked.connect(self.mayores)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def mayores(self):
        from datetime import date
        hoy = date.today()
        listaCompleta = self.t.getAll()
        for fila in listaCompleta:
            fecha = fila[1]
            a, m, d = fecha.split("-")
            edad = hoy.year - int(a)
            if (int(m) > hoy.month) or (int(m) > hoy.month and int(d) > hoy.day):
                edad -= 1
            if edad >= 18:
                print(fila[0])
        

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
