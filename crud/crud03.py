from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QFormLayout, QAbstractItemView, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from clase_sqlite import Database

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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        def instance(lay, clase):
            v = clase
            lay.addWidget(v)
            return v

        self.alumnos = alumnos = Database("Alumno")
        data = alumnos.select()
        header = ["id", "Nombre", "Fecha de Nacimiento", "Comisión", "Nota"]
        table = self.table = Table(data, header)
        table.setFont(QFont("NovaMono", 13))
        table.setSortingEnabled(True)
        # Seleccionar toda la fila
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Dibujar el fondo usando colores alternados
        self.table.setAlternatingRowColors(True)
        self.f = formulario = QFormLayout()
        self.table.itemDoubleClicked.connect(self.printCelda)

        for title in header:
            formulario.addRow(title, QLineEdit())
        
        layout = QVBoxLayout()
        layout.addLayout(formulario)
        botonSeleccionarFila = QPushButton("Seleccionar fila")        
        botonSeleccionarFila.clicked.connect(self.seleccionarFila)
        layout.addWidget(botonSeleccionarFila)
        botonEliminarFila = QPushButton("Eliminar fila")
        botonEliminarFila.clicked.connect(self.eliminarFila)
        layout.addWidget(botonEliminarFila)
        layout.addWidget(self.table)
        


        centralWidget = QWidget()
        centralWidget.setStyleSheet("background-color: skyblue")
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def printCelda(self, celda):
        print(celda.text())

    def seleccionarFila(self):
            filaSeleccionada = self.table.selectedItems()
            formAlumno = self.findChildren(QLineEdit)
            for campoForm, campoGrid in zip(formAlumno, filaSeleccionada):
                campoForm.setText(campoGrid.text())

    def eliminarFila(self):
        filaSeleccionada = self.table.selectedItems()
        if filaSeleccionada:
            fila = filaSeleccionada[0].row()
            fid = self.table.item(fila,0).text()
            print(fid)
            self.table.removeRow(fila)
            self.table.clearSelection()
            self.alumnos.delete(fid)
        else:
            QMessageBox.critical(self, "Eliminar fila", "Seleccione una fila.   ",
                                 QMessageBox.Ok)

            # To Delete or Modify?
            #fila = filaSeleccionada[0].row()
            #self.table.removeRow(fila)
         

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.setGeometry(1000, 100, 700, 500)
    window.show()
    app.exec()

