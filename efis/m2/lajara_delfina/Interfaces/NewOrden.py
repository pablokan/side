from PySide6.QtWidgets import (QComboBox,QMessageBox,QLineEdit,QPushButton,QGridLayout,QTableWidgetItem,QTableWidget,QWidget,QVBoxLayout,QLabel)
from PySide6.QtCore import Qt
from BaseDeDato.database import Database
from Validaciones.Validaciones import *
from Interfaces.AdmCliente import VentanaCliente
from Interfaces.Search.DetallPed import DetallePedido

class NewOrden(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(612, 500)
        self.setWindowTitle("Nueva Orden - Seleccione Cliente...")                    
        layout = QVBoxLayout()
        self.lblOrdenlet = QLabel("Orden Numero:") 
        
        UltimoRegistro = self.ObtenerNumOrden()        
        OrdenNumero = int(UltimoRegistro[0][0]) + 1
        self.lblOrdennum = QLabel("...") 
        self.lblOrdennum.setText(str(OrdenNumero))

        self.lblSel = QLabel("Seleccione Cliente...") 
        self.lblSeleccione = QLabel("Buscar Por:")
        self.ListaMen = QComboBox()        
        self.ListaMen.addItems(["Nombre", "Apelido", "DNI"])
        self.btnBuscar = QPushButton('Buscar')
        self.btnBuscar.clicked.connect(self.ConsultarDatoCliente)
        self.txtBus = QLineEdit()        
        self.txtBus.setPlaceholderText("Ingrese...")
        self.btnDefault = QPushButton('Default')
        self.btnDefault.clicked.connect(self.CargarGrillaDatos)        
                                 
        self.grid = QGridLayout()
        self.grid.addWidget(self.lblOrdenlet, 0, 0)
        self.grid.addWidget(self.lblOrdennum, 0, 1)        
        self.grid.addWidget(self.lblSel, 3, 0)
        self.grid.addWidget(self.btnDefault, 0, 3)        
        self.grid.addWidget(self.lblSeleccione, 2, 0)
        self.grid.addWidget(self.ListaMen, 2, 1)     
        self.grid.addWidget(self.txtBus, 2, 2)     
        self.grid.addWidget(self.btnBuscar, 2, 3)  
        layout.addLayout(self.grid)                                                 

        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(['Id', 'Nombre', 'Apellido', 'FechaNac', 'DNI'])                
        self.table.setAlternatingRowColors(True)        
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection) 
        self.table.setColumnHidden(0,True)                       
        layout.setAlignment(Qt.AlignTop)
        layout.addWidget(self.table)
        
        self.btnNuevo = QPushButton('Crear Orden')
        self.btnNuevo.clicked.connect(self.Mostrar_VentanaDetallOrden) 
        self.btnConsultar = QPushButton('Nuevo Cliente')
        self.btnConsultar.clicked.connect(self.Mostrar_VentanaCliente) 
        self.btnSalir = QPushButton('Salir')
        self.btnSalir.clicked.connect(self.close) 
        GridBotnes = QGridLayout() 
        GridBotnes.addWidget(self.btnNuevo, 0, 0)
        GridBotnes.addWidget(self.btnConsultar, 0, 1)
        GridBotnes.addWidget(self.btnSalir, 0, 2)
        layout.addLayout(GridBotnes)

        self.CargarGrillaDatos()
        self.setLayout(layout)

    def Mostrar_VentanaDetallOrden(self): 
        selected = self.table.currentIndex()
        if not selected.isValid() or len(self.table.selectedItems()) < 1:
            dialogo = QMessageBox.information(self, "Informacion", "Seleccione Dato.") 
            return           
        self.table.setColumnHidden(0,False) 
        ids = self.table.selectedItems()[0]        
        Nombre = self.table.selectedItems()[1]
        Apellido = self.table.selectedItems()[2]        
        self.table.setColumnHidden(0,True)
        dialogo = QMessageBox.information(self, "Informacion", "Orden Ingresada... Interfas no esta terminada...")        
        self.subventana = DetallePedido(ids.text(),f"{Apellido.text()}, {Nombre.text()}")
        self.subventana.show()
        
    def Mostrar_VentanaCliente(self):    
        self.subventana = VentanaCliente()
        self.subventana.show()

    def ConsultarDatoCliente(self):
        base = Database("Clientes","Nombre","Apelido","FechaNac","DNI")
        Clientes = base.selectBuscarCliente(self.ListaMen.currentText(),self.txtBus.text())        
        self.GrillaDatos(Clientes)

    def CargarGrillaDatos(self):
        base = Database("Clientes","Nombre","Apelido","FechaNac","DNI")
        Clientes = base.select()
        self.GrillaDatos(Clientes)
            
    def ObtenerNumOrden(self):
        base = Database("OrdenFac","idcliente","Total")
        NumOrden = base.ObtenerUltimoRegistro()
        return NumOrden

    def GrillaDatos(self,Clientes):
        FilaContador = 0
        self.table.setRowCount(0 + len(Clientes))
        for Client in Clientes:                                    
            self.table.setItem(FilaContador, 0, QTableWidgetItem(f"{Client[0]}"))
            self.table.setItem(FilaContador, 1, QTableWidgetItem(f"{Client[1]}"))
            self.table.setItem(FilaContador, 2, QTableWidgetItem(f"{Client[2]}"))
            self.table.setItem(FilaContador, 3, QTableWidgetItem(f"{Client[3]}"))
            self.table.setItem(FilaContador, 4, QTableWidgetItem(f"{Client[4]}"))
            FilaContador += 1

    def mostrar_info(self):
        dialogo = QMessageBox.information(
            self, "Informacion", "Lo siento, Creandola...")  