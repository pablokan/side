import os, sys
sys.path.append(os.path.abspath('libs'))
from PySide6.QtWidgets import (QApplication, QFormLayout, QDialog, QPushButton, QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, QMenu, QMessageBox, QWidget, QMainWindow, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout)
from PySide6.QtGui import (QIntValidator, QFont)
from datetime import date, datetime
import sqlite3

class InputInt(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setValidator(QIntValidator())

class Fecha():
    def fechaActual(self):
        hoy=date.today()
        return hoy.strftime("%d/%m/%Y")

def defaultWindow(ventana):
    ventana.resize(800,600)
    ventana.show()

def casillaTabla(casilla, layout, movimientoH, movimientoV):
    colorLetra = '*{;color: #dcdcaa}'
    casilla.setStyleSheet(colorLetra)
    casilla.move(movimientoH, movimientoV)
    casilla.setFont(QFont("Arial", 22))
    layout.addWidget(casilla)

def guardado(string, claves, tabla):
    baseClientes = sqlite3.connect("database.db")
    cur = baseClientes.cursor()
    cur.execute(f"INSERT INTO {tabla} ({claves}) VALUES ({string});")#''
    baseClientes.commit()
    baseClientes.close()

def actualizar(string, claves, tabla, id):
    baseClientes = sqlite3.connect("database.db")
    cur = baseClientes.cursor()
    cur.execute(f"REPLACE {tabla} SET ({claves}) VALUES ({string}) WHERE id={id};")#''
    baseClientes.commit()
    baseClientes.close()


def borrado(tabla, id):
    base = sqlite3.connect("database.db")
    base.execute(f"DELETE FROM {tabla} WHERE id = {id}")
    base.commit()
    base.close()

def tituloTabla(texto, layout, movimientoH, movimientoV):
    texto.setFixedWidth(350)
    colorLetra = '*{;color: #dcdcaa}'
    texto.setStyleSheet(colorLetra)
    texto.move(movimientoH, movimientoV)
    texto.setFont(QFont("Arial", 22))
    layout.addWidget(texto)

def botonTabla(self, contenido, movimientoH, movimientoV, funcion):
    self.boton = QPushButton(contenido, self)
    self.boton.setFixedWidth(140)
    colorLetra = '*{;color: #dcdcaa}'
    self.boton.setStyleSheet(colorLetra)
    self.boton.move(movimientoH, movimientoV)
    self.boton.setFont(QFont("Arial", 22))
    self.boton.clicked.connect(funcion)

def botonMainMenu(boton, layout, funcion):
    boton.setFixedWidth(140)
    boton.setFont(QFont("Arial", 22))
    colorLetra = '*{;color: #dcdcaa}'
    boton.setStyleSheet(colorLetra)
    layout.addWidget(boton)
    boton.clicked.connect(funcion)

def datosTabla(self, claveColumnas, base):
    baseClientes = sqlite3.connect("database.db")
    cur = baseClientes.cursor()
    cur.execute(f"SELECT {claveColumnas} FROM {base}")
    datosClientes = cur.fetchall()

    self.clientesTabla.clearContents()
    self.clientesTabla.setRowCount(len(datosClientes))

    for (indexRow, row) in enumerate(datosClientes):
        for (indexCell, cell) in enumerate(row):
            self.clientesTabla.setItem(indexRow, indexCell, QTableWidgetItem(str(cell)))

def configurarTabla(self, nombreColumnas, claveColumnas, base):
    self.clientesTabla = QTableWidget(self)
    self.clientesTabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
    self.clientesTabla.setDragDropOverwriteMode(False)
    self.clientesTabla.setSelectionBehavior(QAbstractItemView.SelectRows)
    self.clientesTabla.setSelectionMode(QAbstractItemView.SingleSelection)
    self.clientesTabla.setWordWrap(False)
    self.clientesTabla.setSortingEnabled(True)
    self.clientesTabla.setColumnCount(len(nombreColumnas))
    self.clientesTabla.setRowCount(0)
    self.clientesTabla.horizontalHeader().setHighlightSections(False)
    self.clientesTabla.horizontalHeader().setStretchLastSection(True)
    self.clientesTabla.verticalHeader().setVisible(False)
    self.clientesTabla.setAlternatingRowColors(False)
    self.clientesTabla.verticalHeader().setDefaultSectionSize(20)
    self.clientesTabla.setHorizontalHeaderLabels(nombreColumnas)

    for self.indice, self.ancho in enumerate((100,100),start=0):
        self.clientesTabla.setColumnWidth(self.indice, self.ancho)
    self.clientesTabla.resize(780, 300)
    self.clientesTabla.move(20, 56)
    css = '*{background-color: grey; color: #1e1e1e;}'
    self.clientesTabla.setStyleSheet(css)
    datosTabla(self, claveColumnas, base)
    return self.clientesTabla