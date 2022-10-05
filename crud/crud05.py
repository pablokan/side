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

class Line(Text):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(f"background-color: black; font-size:3px; margin: 5px")

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
        fieldKeys = list(header.keys())[1:]
        self.alumnos = alumnos = Database("Alumno", *fieldKeys)

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

        for title in header.values():
            formulario.addRow(Text(title), Input())

        layout = QVBoxLayout()

        formBase = self.formBase = QWidget()
        formBase.setHidden(True)
        layout.addWidget(formBase) 
        formBase.setLayout(formulario)
        #layout.addLayout(formulario)
        layout.addWidget(Line())
        bNew = Button("Nuevo")
        bNew.clicked.connect(self.newRecord)
        botonera.addWidget(bNew)
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
        layout.addWidget(Line())
        self.search = Input("Buscar por nombre", foreg="white", backg="blue")
        layout.addWidget(self.search)
        self.search.textChanged.connect(self.update_filter)
        layout.addWidget(self.table)
    
        centralWidget = QWidget()
        centralWidget.setStyleSheet("background-color: skyblue")
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)


    def newRecord(self):
        self.formBase.setHidden(False)

    def onClicked(self):
        self.selRow = self.table.selectedItems()
        formAlumno = self.findChildren(Input)
        roID = 0
        for campoForm, campoGrid in zip(formAlumno, self.selRow):
            campoForm.setText(campoGrid.text())
            if roID == 0:
                campoForm.setReadOnly(True)
                campoForm.setDisabled(True)
                roID += 1

    def update_filter(self):
        name = self.search.text().lower()
        for row in range(self.table.rowCount()):
            item = self.table.item(row, 1)
            self.table.setRowHidden(row, name not in item.text().lower())

    def printCelda(self, celda):
        print(celda.text())

    def insertRecord(self):
        record = [r.text() for r in self.findChildren(Input)[1:-1]]
        self.alumnos.insert(*record)
        self.table.insertRow(0)
        for i, celda in enumerate(record, start=1):
            if celda.isdigit():
                celda = int(celda)
            item = QTableWidgetItem(celda)
            item.setData(Qt.DisplayRole, celda) # para que ordene por numeración
            self.table.setItem(0, i, item)

    def updateRecord(self):
        record = [r.text() for r in self.findChildren(Input)[:-1]]
        print(f'Debugging ######## {record=} #########')
        self.alumnos.update(*record)
        selRow = self.table.selectedItems()
        print(f'Debugging ######## {selRow[0].row()=} #########')
        r = int(selRow[0].row())
        for c, celda in enumerate(record, start=0):
            if celda.isdigit():
                celda = int(celda)
            item = QTableWidgetItem(celda)
            item.setData(Qt.DisplayRole, celda) # para que ordene por numeración
            self.table.setItem(r, c, item)
        

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
    window.resize(700, 800)
    window.show()
    app.exec()

