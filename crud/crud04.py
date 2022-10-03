import os, sys
from pprint import pprint
sys.path.append(os.path.abspath('libs'))

from PySide6.QtWidgets import (
    QApplication, QWidget, QMainWindow, 
    QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QAbstractItemView, QFormLayout, QMessageBox)

from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from styles import Text, Input, Button

from database import Database

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

        header = {
            "id": "Identificador", 
            "nombre": "Nombre", 
            "fecha_nac": "Fecha de Nacimiento", 
            "comision": "Comisión", 
            "nota": "Nota"
            }
        # "Alumno", *list(header.keys())    
        fields = list(header.keys())
        self.alumnos = alumnos = Database("Alumno", *fields)

        data = alumnos.select()
        table = self.table = Table(data, header)
        table.setTabKeyNavigation(False)
        table.itemClicked.connect(self.onClicked)
        table.setFont(QFont("NovaMono", 13))
        table.setSortingEnabled(True)
        # Seleccionar toda la fila
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Dibujar el fondo usando colores alternados
        self.table.setAlternatingRowColors(True)
        self.f = formulario = QFormLayout()
        botonera = QHBoxLayout()

        self.table.itemDoubleClicked.connect(self.printCelda)

        self.search = Input()
        formulario.addRow(Text('Buscar'), self.search)
        self.search.textChanged.connect(self.update_filter)
        
        for title in header.values():
            formulario.addRow(Text(title), Input())

        layout = QVBoxLayout()
        layout.addLayout(formulario)
        bInsert = Button("Agregar")        
        bInsert.clicked.connect(self.insertRecord)
        botonera.addWidget(bInsert)
        bUpdate = Button("Modificar")        
        bUpdate.clicked.connect(self.updateRecord)
        botonera.addWidget(bUpdate)
        bDelete = Button("Eliminar")
        bDelete.clicked.connect(self.deleteRecord)
        botonera.addWidget(bDelete)
        layout.addLayout(botonera)
        layout.addWidget(self.table)
    
        centralWidget = QWidget()
        centralWidget.setStyleSheet("background-color: skyblue")
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def onClicked(self):
        self.selRow = self.table.selectedItems()
        formAlumno = self.findChildren(Input)[1:]
        roID = 0
        for campoForm, campoGrid in zip(formAlumno, self.selRow):
            campoForm.setText(campoGrid.text())
            if roID == 0:
                campoForm.setReadOnly(True)
                roID += 1

    def update_filter(self):
        name = self.search.text().lower()
        for row in range(self.table.rowCount()):
            item = self.table.item(row, 0)
            self.table.setRowHidden(row, name not in item.text().lower())

    def printCelda(self, celda):
        print(celda.text())

    def insertRecord(self):
        record = [r.text() for r in self.findChildren(Input)[2:]]
        self.alumnos.insert(*record)
        self.table.insertRow(0)
        for i, celda in enumerate(record, start=1):
            if celda.isdigit():
                celda = int(celda)
            item = QTableWidgetItem(celda)
            item.setData(Qt.DisplayRole, celda) # para que ordene por numeración
            self.table.setItem(0, i, item)

    def updateRecord(self):
        record = [r.text() for r in self.findChildren(Input)[1:]]
        print(f'Debugging ######## {record=} #########')
        self.alumnos.update(*record)
        for i, celda in enumerate(record, start=1):
            if celda.isdigit():
                celda = int(celda)
            item = QTableWidgetItem(celda)
            item.setData(Qt.DisplayRole, celda) # para que ordene por numeración
            self.table.setItem(int(self.selRow[0].text()), i, item)
        

    def deleteRecord(self):
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
    window.resize(700, 1000)
    window.show()
    app.exec()

