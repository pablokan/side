from PySide6.QtWidgets import (QComboBox,QLineEdit,QMessageBox,QPushButton,QGridLayout,QTableWidgetItem,QTableWidget,QWidget,QVBoxLayout,QLabel)
from PySide6.QtCore import Qt
from BaseDeDato.database import Database
from Validaciones.Validaciones import *

class VentanaMenuComidas(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(612, 500)
        self.setWindowTitle("Gestion de menu comida")
        layout = QVBoxLayout()
        self.lblCat1 = QLabel("Categoria:")
        self.ListaMen = QComboBox()
        self.ListaMen.setPlaceholderText("Seleccione...")
        self.ListaMen.addItems(["Pizza", "Milanesa", "Empanadas"]) 
        self.lblNom1 = QLabel("Nombre:")
        self.txtNom1 = QLineEdit()
        self.txtNom1.setValidator(ValidarSolamenteLetras())
        self.txtNom1.setPlaceholderText("Ingrese...")
        self.lblDes = QLabel("Descripcion:")
        self.txtDes = QLineEdit()
        self.txtDes.setValidator(ValidarSolamenteLetras())
        self.txtDes.setPlaceholderText("Ingrese...")  
        self.lblPre = QLabel("Precio:")
        self.txtPre = QLineEdit()
        self.txtPre.setPlaceholderText("$...")
        self.txtPre.setValidator(ValidarSolamenteNumeros())   
        self.btnInsertar = QPushButton('Insertar')
        self.btnInsertar.clicked.connect(self.insertarDatosComidas)        
        self.btnModificar = QPushButton('Modificar')
        self.btnModificar.clicked.connect(self.ModificarDatoComidas)  
        self.btnModificar.setEnabled(False)
        self.btnEliminar = QPushButton('Eliminar')
        self.btnEliminar.clicked.connect(self.eliminarDatosComidas)
        self.btnCargar = QPushButton('Cargar')
        self.btnCargar.clicked.connect(self.CargarDatosComidas) 
        
        self.grid = QGridLayout()
        self.grid.addWidget(self.lblCat1, 1, 0)
        self.grid.addWidget(self.ListaMen, 1, 1)
        self.grid.addWidget(self.btnInsertar, 1, 2)  
        self.grid.addWidget(self.lblNom1, 2, 0)
        self.grid.addWidget(self.txtNom1, 2, 1)
        self.grid.addWidget(self.btnModificar, 2, 2) 
        self.grid.addWidget(self.lblDes, 3, 0)
        self.grid.addWidget(self.txtDes, 3, 1)
        self.grid.addWidget(self.btnEliminar, 3, 2)  
        self.grid.addWidget(self.lblPre, 4, 0)
        self.grid.addWidget(self.txtPre, 4, 1)         
        self.grid.addWidget(self.btnCargar, 4, 2)
        layout.addLayout(self.grid)

        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(['Id', 'Categoria', 'Nombre', 'Descripcion', 'Precio'])
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
        self.txtNom1.setText("")
        self.txtDes.setText("")
        self.txtPre.setText("")
        self.table.setColumnHidden(0,True)
        self.btnModificar.setEnabled(False)
        self.btnCargar.setEnabled(True)
        self.btnInsertar.setEnabled(True)
        self.btnEliminar.setEnabled(True)
        self.table.setEnabled(True) 

    def CargarGrillaDatos(self):
        base = Database("Comidas","Categoria","Nombre","Descripcion","Precio")
        Menus = base.select()
        FilaContador = 0
        self.table.setRowCount(0 + len(Menus))
        for Menu in Menus:                        
            self.table.setItem(FilaContador, 0, QTableWidgetItem(f"{Menu[0]}"))
            self.table.setItem(FilaContador, 1, QTableWidgetItem(f"{Menu[1]}"))
            self.table.setItem(FilaContador, 2, QTableWidgetItem(f"{Menu[2]}"))
            self.table.setItem(FilaContador, 3, QTableWidgetItem(f"{Menu[3]}"))
            self.table.setItem(FilaContador, 4, QTableWidgetItem(f"$ {Menu[4]}"))
            FilaContador += 1

    def insertarDatosComidas(self):
        base = Database("Comidas","Categoria","Nombre","Descripcion","Precio")
        if (self.txtNom1.text() == "") or (self.txtDes.text() == "") or (self.txtPre.text() == ""):
            dialogo = QMessageBox.information(self, "Informacion", "Faltan ingresar datos")
        else:
            base.insert(f"{self.ListaMen.currentText()}",f"{self.txtNom1.text()}",f"{self.txtDes.text()}",f"{self.txtPre.text()}")        
            self.CargarGrillaDatos()
            dialogo = QMessageBox.information(self, "Informacion", "Dato Insertado...")
            self.NuevoDato()

    def ModificarDatoComidas(self):
        self.table.setColumnHidden(0,False)
        ids = self.table.selectedItems()[0]
        self.table.setColumnHidden(0,True)        
        base = Database("Comidas","Categoria","Nombre","Descripcion","Precio")
        base.update(ids.text(),f"{self.ListaMen.currentText()}",f"{self.txtNom1.text()}",f"{self.txtDes.text()}",f"{self.txtPre.text()}")
        self.CargarGrillaDatos()
        dialogo = QMessageBox.information(self, "Informacion", "Dato Modificado...")  
        self.NuevoDato()
        self.btnModificar.setEnabled(False)
        self.btnCargar.setEnabled(True)
        self.btnInsertar.setEnabled(True)
        self.btnEliminar.setEnabled(True)
        self.table.setEnabled(True) 

    def eliminarDatosComidas(self):
        selected = self.table.currentIndex()
        if not selected.isValid() or len(self.table.selectedItems()) < 1:
            dialogo = QMessageBox.information(self, "Informacion", "Seleccione Dato...") 
            return 
        self.table.setColumnHidden(0,False)
        ids = self.table.selectedItems()[0]
        self.table.setColumnHidden(0,True)
        base = Database("Comidas","Categoria","Nombre","Descripcion","Precio")
        base.delete(ids.text())
        self.CargarGrillaDatos()
        dialogo = QMessageBox.information(self, "Informacion", "Dato Eliminado...") 
        self.NuevoDato()

    def CargarDatosComidas(self):
        selected = self.table.currentIndex()
        if not selected.isValid() or len(self.table.selectedItems()) < 1:
            dialogo = QMessageBox.information(self, "Informacion", "Seleccione Dato...") 
            return
        self.table.setColumnHidden(0,False)
        ids = self.table.selectedItems()[1]                       
        self.ListaMen.clear()
        self.ListaMen.addItems(["Pizza", "Milanesa", "Empanadas"])
        self.ListaMen.setPlaceholderText(ids.text())        
        ids = self.table.selectedItems()[2]                       
        self.txtNom1.setText(ids.text())
        ids = self.table.selectedItems()[3]                       
        self.txtDes.setText(ids.text())
        ids = self.table.selectedItems()[4]                       
        self.txtPre.setText(ids.text()[2:])
        self.table.setColumnHidden(0,True)
        self.btnModificar.setEnabled(True)
        self.btnCargar.setEnabled(False)
        self.btnInsertar.setEnabled(False)
        self.btnEliminar.setEnabled(False)
        self.table.setEnabled(False)

    def mostrar_info(self):
        dialogo = QMessageBox.information(
            self, "Informacion", "Lo siento, Creandola...") 