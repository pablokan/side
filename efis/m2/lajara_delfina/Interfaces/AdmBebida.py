from PySide6.QtWidgets import (QLineEdit,QMessageBox,QPushButton,QGridLayout,QTableWidgetItem,QTableWidget,QWidget,QVBoxLayout,QLabel)
from PySide6.QtCore import Qt
from BaseDeDato.database import Database
from Validaciones.Validaciones import *

class VentanaBebidas(QWidget):
    def __init__(self):
        super().__init__()        
        self.resize(612, 500)
        self.setWindowTitle("Administracion Bebidas")            
        layout = QVBoxLayout()
        self.lblMarc = QLabel("Marca:")
        self.txtMarc = QLineEdit()
        self.txtMarc.setPlaceholderText("Ingrese...")         
        self.txtMarc.setValidator(ValidarSolamenteLetras())  
        self.lblPrecio = QLabel("Precio:")
        self.txtPrecio = QLineEdit()
        self.txtPrecio.setPlaceholderText("$...")
        self.txtPrecio.setValidator(ValidarSolamenteNumeros())  
        
        self.btnInsertar = QPushButton('Insertar')
        self.btnInsertar.clicked.connect(self.insertarDatos)        
        self.btnModificar = QPushButton('Modificar')
        self.btnModificar.setEnabled(False)
        self.btnModificar.clicked.connect(self.ModificarDato)  
        self.btnEliminar = QPushButton('Eliminar')
        self.btnEliminar.clicked.connect(self.eliminarDatos)
        self.btnCargar = QPushButton('Cargar')
        self.btnCargar.clicked.connect(self.CargarDatos)  

        self.grid = QGridLayout() 
        self.grid.addWidget(self.lblMarc, 1, 0)
        self.grid.addWidget(self.txtMarc, 1, 1)
        self.grid.addWidget(self.btnInsertar, 1, 2)
        self.grid.addWidget(self.lblPrecio, 2, 0)
        self.grid.addWidget(self.txtPrecio, 2, 1)
        self.grid.addWidget(self.btnModificar, 2, 2)                
        self.grid.addWidget(self.btnEliminar, 3, 2)                 
        self.grid.addWidget(self.btnCargar, 4, 2)
        layout.addLayout(self.grid)                                                     

        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(['Id', 'Marca', 'Precio'])                
        self.table.setAlternatingRowColors(True)        
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection) 
        self.table.setColumnHidden(0,True)                       
        layout.setAlignment(Qt.AlignTop)
        layout.addWidget(self.table)

        self.btnNuevo = QPushButton('Default')
        self.btnNuevo.clicked.connect(self.NuevoDato) 
        self.btnConsultar = QPushButton('Consultar')
        self.btnConsultar.clicked.connect(self.mostrar_info) 
        self.btnSalir = QPushButton('Salir')
        self.btnSalir.clicked.connect(self.close) 
        GridBotnes = QGridLayout() 
        GridBotnes.addWidget(self.btnNuevo, 0, 0)
        # GridBotnes.addWidget(self.btnConsultar, 0, 1)
        GridBotnes.addWidget(self.btnSalir, 0, 2)
        layout.addLayout(GridBotnes)

        self.CargarGrillaDatos()
        self.setLayout(layout)
        
    def NuevoDato(self):
        self.txtMarc.setText("")
        self.txtPrecio.setText("")        
        self.table.setColumnHidden(0,True)
        self.btnModificar.setEnabled(False)
        self.btnCargar.setEnabled(True)
        self.btnInsertar.setEnabled(True)
        self.btnEliminar.setEnabled(True)
        self.table.setEnabled(True) 

    def CargarGrillaDatos(self):
        base = Database("Bebidas","Marca","Precio")
        Clientes = base.select()
        FilaContador = 0
        self.table.setRowCount(0 + len(Clientes))
        for Client in Clientes:                                    
            self.table.setItem(FilaContador, 0, QTableWidgetItem(f"{Client[0]}"))
            self.table.setItem(FilaContador, 1, QTableWidgetItem(f"{Client[1]}"))
            self.table.setItem(FilaContador, 2, QTableWidgetItem(f"$ {Client[2]}"))
            FilaContador += 1

    def insertarDatos(self):        
        base = Database("Bebidas","Marca","Precio")       
        if (self.txtMarc.text() == "") or (self.txtPrecio.text() == ""):
            dialogo = QMessageBox.information(self, "Informacion", "Faltan ingresar datos")
        else:
            base.insert(f"{self.txtMarc.text()}",f"{self.txtPrecio.text()}")        
            self.CargarGrillaDatos()
            dialogo = QMessageBox.information(self, "Informacion", "Dato Insertado...")
            self.NuevoDato()
        
    def eliminarDatos(self):
        selected = self.table.currentIndex()
        if not selected.isValid() or len(self.table.selectedItems()) < 1:
            dialogo = QMessageBox.information(self, "Informacion", "Seleccione Dato...") 
            return
        self.table.setColumnHidden(0,False) 
        ids = self.table.selectedItems()[0]
        self.table.setColumnHidden(0,True)
        base = Database("Bebidas","Marca","Precio")
        base.delete(ids.text())
        self.CargarGrillaDatos()
        dialogo = QMessageBox.information(self, "Informacion", "Dato Eliminado...") 
        self.NuevoDato()

    def CargarDatos(self):  
        selected = self.table.currentIndex()
        if not selected.isValid() or len(self.table.selectedItems()) < 1:
            dialogo = QMessageBox.information(self, "Informacion", "Seleccione Dato...") 
            return
        self.table.setColumnHidden(0,False) 
        ids = self.table.selectedItems()[1]                       
        self.txtMarc.setText(ids.text())
        ids = self.table.selectedItems()[2]                       
        self.txtPrecio.setText(ids.text()[2:])        
        self.table.setColumnHidden(0,True)
        self.btnModificar.setEnabled(True)
        self.btnCargar.setEnabled(False)
        self.btnInsertar.setEnabled(False)
        self.btnEliminar.setEnabled(False)
        self.table.setEnabled(False)

    def ModificarDato(self):               
        base = Database("Bebidas","Marca","Precio")
        self.table.setColumnHidden(0,False)
        ids = self.table.selectedItems()[0] 
        base.update(ids.text(),f"{self.txtMarc.text()}",f"{self.txtPrecio.text()}")
        self.CargarGrillaDatos()
        self.table.setColumnHidden(0,True)
        dialogo = QMessageBox.information(self, "Informacion", "Dato Modificado...")  
        self.NuevoDato()
        self.btnModificar.setEnabled(False)
        self.btnCargar.setEnabled(True)
        self.btnInsertar.setEnabled(True)
        self.btnEliminar.setEnabled(True)
        self.table.setEnabled(True) 

    def mostrar_info(self):
        dialogo = QMessageBox.information(
            self, "Informacion", "Lo siento, Creandola...")  