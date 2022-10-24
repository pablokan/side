from PySide6.QtWidgets import (QDateEdit,QComboBox,QLineEdit,QMessageBox,QPushButton,QGridLayout,QTableWidgetItem,QTableWidget,QWidget,QVBoxLayout,QLabel)
from PySide6.QtCore import Qt,QDate
from BaseDeDato.database import Database
from Validaciones.Validaciones import *

class VentanaCliente(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(612, 500)
        self.setWindowTitle("Administracion Cliente")            
        layout = QVBoxLayout()
        self.lblName = QLabel("Nombre:")
        self.txtName = QLineEdit()
        self.txtName.setPlaceholderText("Ingrese...")         
        self.txtName.setValidator(ValidarSolamenteLetras())            
        self.lblApellido = QLabel("Apellido:")
        self.txtApellido = QLineEdit()
        self.txtApellido.setPlaceholderText("Ingrese...")
        self.txtApellido.setValidator(ValidarSolamenteLetras())        
        self.lblFechaNac = QLabel("Fecha Nac.:")
        self.txtFechaNac = QDateEdit()
        self.txtFechaNac.setDisplayFormat("dd/MM/yyyy")  
        self.lblDNI = QLabel("DNI:")
        self.txtDNI = QLineEdit()
        self.txtDNI.setPlaceholderText("Ingrese...") 
        self.txtDNI.setValidator(ValidarSolamenteDNI())
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
        self.grid.addWidget(self.lblName, 1, 0)
        self.grid.addWidget(self.txtName, 1, 1)
        self.grid.addWidget(self.btnInsertar, 1, 2)
        self.grid.addWidget(self.lblApellido, 2, 0)
        self.grid.addWidget(self.txtApellido, 2, 1)
        self.grid.addWidget(self.btnModificar, 2, 2)
        self.grid.addWidget(self.lblFechaNac, 3, 0)
        self.grid.addWidget(self.txtFechaNac, 3, 1)
        self.grid.addWidget(self.btnEliminar, 3, 2) 
        self.grid.addWidget(self.lblDNI, 4, 0)
        self.grid.addWidget(self.txtDNI, 4, 1)
        self.grid.addWidget(self.btnCargar, 4, 2)
        layout.addLayout(self.grid)  

        self.lbldatos = QLabel("Consultar Por:")  
        self.lbldatos.setEnabled(False) 
        self.ListaConsultar = QComboBox()        
        self.ListaConsultar.addItems(["Nombre","Apelido","DNI"]) 
        self.ListaConsultar.setEnabled(False)
        self.txtdatos = QLineEdit()
        self.txtdatos.setPlaceholderText("Ingrese:") 
        self.txtdatos.setEnabled(False)
        self.BtnConsultar = QPushButton('Consultar')
        self.BtnConsultar.clicked.connect(self.ConsultarDatoCliente)
        self.BtnConsultar.setEnabled(False)             

        self.gridconsultar = QGridLayout()         
        self.gridconsultar.addWidget(self.lbldatos,0,0)
        self.gridconsultar.addWidget(self.ListaConsultar,0,1)
        self.gridconsultar.addWidget(self.txtdatos,0,2)
        self.gridconsultar.addWidget(self.BtnConsultar,0,3)                              
        layout.addLayout(self.gridconsultar)      

        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(['Id', 'Nombre', 'Apellido', 'FechaNac', 'DNI'])                
        self.table.setAlternatingRowColors(True)        
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection) 
        self.table.setColumnHidden(0,True)                       
        layout.setAlignment(Qt.AlignTop)
        layout.addWidget(self.table)

        self.btnNuevo = QPushButton('Default')
        self.btnNuevo.clicked.connect(self.NuevoDato) 
        self.btnConsultar = QPushButton('Activar Consulta')
        self.btnConsultar.clicked.connect(self.ConsultarDato) 
        self.btnSalir = QPushButton('Salir')
        self.btnSalir.clicked.connect(self.close) 
        GridBotnes = QGridLayout() 
        GridBotnes.addWidget(self.btnNuevo, 0, 0)
        GridBotnes.addWidget(self.btnConsultar, 0, 1)
        GridBotnes.addWidget(self.btnSalir, 0, 2)
        layout.addLayout(GridBotnes)

        self.CargarGrillaDatos()
        self.setLayout(layout)
        
    def NuevoDato(self):
        self.txtName.setText("")
        self.txtApellido.setText("")
        self.txtDNI.setText("")
        self.table.setColumnHidden(0,True)
        self.btnModificar.setEnabled(False)
        self.btnCargar.setEnabled(True)
        self.btnInsertar.setEnabled(True)
        self.btnEliminar.setEnabled(True)
        self.table.setEnabled(True) 
        self.CargarGrillaDatos()
        self.BtnConsultar.setEnabled(False)
        self.lbldatos.setEnabled(False) 
        self.ListaConsultar.setEnabled(False)
        self.txtdatos.setEnabled(False)
        self.btnInsertar.setEnabled(True)
        self.txtApellido.setEnabled(True)
        self.txtFechaNac.setEnabled(True)
        self.txtName.setEnabled(True)
        self.txtDNI.setEnabled(True)

    def ConsultarDato(self):
        self.BtnConsultar.setEnabled(True)
        self.lbldatos.setEnabled(True) 
        self.ListaConsultar.setEnabled(True)
        self.txtdatos.setEnabled(True)
        self.btnInsertar.setEnabled(False)
        self.txtApellido.setEnabled(False)
        self.txtFechaNac.setEnabled(False)
        self.txtName.setEnabled(False)
        self.txtDNI.setEnabled(False)

    def ConsultarDatoCliente(self):
        base = Database("Clientes","Nombre","Apelido","FechaNac","DNI")
        Clientes = base.selectBuscarCliente(self.ListaConsultar.currentText(),self.txtdatos.text())        
        self.GrillaDatos(Clientes)

    def CargarGrillaDatos(self):
        base = Database("Clientes","Nombre","Apelido","FechaNac","DNI")
        Clientes = base.select()
        self.GrillaDatos(Clientes)
        
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

    def insertarDatos(self):        
        base = Database("Clientes","Nombre","Apelido","FechaNac","DNI")        
        if (self.txtName.text() == "") or (self.txtApellido.text() == "") or (self.txtDNI.text() == ""):
            dialogo = QMessageBox.information(self, "Informacion", "Faltan ingresar datos")
        else:
            base.insert(f"{self.txtName.text()}",f"{self.txtApellido.text()}",f"{self.txtFechaNac.text()}",f"{self.txtDNI.text()}")        
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
        base = Database("Clientes","Nombre","Apelido","FechaNac","DNI")
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
        self.txtName.setText(ids.text())
        ids = self.table.selectedItems()[2]                       
        self.txtApellido.setText(ids.text())
        ids = self.table.selectedItems()[3]    
        FechaNacimiento = QDate.fromString(ids.text(), "dd/MM/yyyy")                
        self.txtFechaNac.setDisplayFormat("dd/MM/yyyy")
        self.txtFechaNac.setDate(FechaNacimiento)  
        ids = self.table.selectedItems()[4]                       
        self.txtDNI.setText(ids.text())
        self.table.setColumnHidden(0,True)
        self.btnModificar.setEnabled(True)
        self.btnCargar.setEnabled(False)
        self.btnInsertar.setEnabled(False)
        self.btnEliminar.setEnabled(False)
        self.table.setEnabled(False)
        self.btnInsertar.setEnabled(False)
        self.txtApellido.setEnabled(True)
        self.txtFechaNac.setEnabled(True)
        self.txtName.setEnabled(True)
        self.txtDNI.setEnabled(True)
        self.BtnConsultar.setEnabled(False)

    def ModificarDato(self):               
        base = Database("Clientes","Nombre","Apelido","FechaNac","DNI")
        self.table.setColumnHidden(0,False)
        ids = self.table.selectedItems()[0] 
        base.update(ids.text(),f"{self.txtName.text()}",f"{self.txtApellido.text()}",f"{self.txtFechaNac.text()}",f"{self.txtDNI.text()}")
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