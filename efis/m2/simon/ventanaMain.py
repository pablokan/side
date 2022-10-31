import csv

from database import Database

from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout,QLabel,QVBoxLayout, QWidget, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

clientesDB = Database("clientesDB","nombre","articulo","saldo","cantidadCuotas","cuota") #creamos/abrimos la BD

class TablaClientes(QTableWidget):
    def __init__(self,datos):
        super().__init__()
        self.setRowCount(len(datos))
        self.setColumnCount(6)
        self.setHorizontalHeaderLabels(["id","nombre","articulo","saldo","cantidad de cuotas","cuota por mes"])
        for i in range(len(datos)):
            for j in range(len(datos[i])):
                registro = datos[i][j] #registro es cada celda 
                item = QTableWidgetItem(registro)
                item.setData(Qt.DisplayRole, registro) # para que ordene por numeración
                self.setItem(i, j, item) #agregar el registro (item) a la tabla
        self.resizeColumnsToContents()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        datos = clientesDB.select()

        self.setWindowTitle('Clientes')
        self.layout = QGridLayout()
        self.tabla = tabla = TablaClientes(datos)
        self.layout.addWidget(tabla,0,0)
        self.botonEditarCliente = QPushButton("Editar cliente")
        self.layout.addWidget(self.botonEditarCliente,2,0)
        self.botonEditarCliente.setDefault(True)
        self.botonEliminarCliente = QPushButton("Eliminar cliente")
        self.layout.addWidget(self.botonEliminarCliente,3,0)
        self.botonEliminarCliente.setDefault(True)

        centralWidget = QWidget()
        centralWidget.setLayout(self.layout)
        self.setCentralWidget(centralWidget)

    def function_name(self):
        self.texto.setText(f'Hola {self.entrada.text()}')

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()






