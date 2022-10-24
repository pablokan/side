from PySide6.QtWidgets import (QComboBox,QMessageBox,QLineEdit,QPushButton,QGridLayout,QTableWidgetItem,QTableWidget,QWidget,QVBoxLayout,QLabel)
from PySide6.QtCore import Qt,QDate
from BaseDeDato.database import Database
from Validaciones.Validaciones import *

class DetallePedido(QWidget):
    def __init__(self,NumCliente,NomyApeCliente):
        super().__init__()
        self.NumeroCliente = NumCliente
        self.NomnreApellidocliente = NomyApeCliente
        self.resize(612, 500)
        self.setWindowTitle("Detalle Pedido...")                    
        layout = QVBoxLayout()
        self.lblsep = QLabel(" ")        
        self.lblnumorden = QLabel("Nº Orden:") 

        UltimoRegistro = self.ObtenerNumOrden()        
        self.OrdenNumero = int(UltimoRegistro[0][0]) + 1
        self.lblOrdennum = QLabel("...") 
        self.lblOrdennum.setText(str(self.OrdenNumero))

        self.lblSeparador = QLabel("") 
        self.lblSeparador = QLabel()

        self.lblCliente = QLabel("Cliente:") 
        self.lblCli = QLabel()
        self.lblCli.setText(f"{self.NumeroCliente}) {self.NomnreApellidocliente}") 
        self.ListaSecc = QComboBox()
        self.lblSeccion = QLabel("Seccion: ")
        self.ListaSecc.addItems(["Comidas","Bebidas"])
        self.ListaSecc.activated.connect(self.CambioListaSecc)
        
        self.lblSeccion2 = QLabel("Categoria: ")
        self.ListaCat = QComboBox()
        self.ListaCat.addItems([])
        self.ListaCat.setEnabled(False)
        self.ListaCat.activated.connect(self.CambioMenuSecc)

        self.lblSeccion3 = QLabel("Seleccione: ")
        self.ListaCat2 = QComboBox()
        self.ListaCat2.addItems([])
        self.ListaCat2.setEnabled(False)
        self.ListaCat2.activated.connect(self.CambioEstadoRegistro)

        self.lblCantidad = QLabel("Cantidad: ")
        self.ListaCantidad = QComboBox()
        self.ListaCantidad.addItems(["1","2","3","4","5","6","7","8","9","10"])
        self.ListaCantidad.activated.connect(self.CambioListaCantidad)

        self.btnAgregarDato = QPushButton('Agregar al pedido')
        self.btnAgregarDato.clicked.connect(self.mostrar_info)
        self.btnEliminarDato = QPushButton('Eliminar')
        self.btnEliminarDato.clicked.connect(self.mostrar_info)
        self.btnModificarReg = QPushButton('Modificar')
        self.btnModificarReg.clicked.connect(self.mostrar_info)
        self.btnCargarReg = QPushButton('Cargar')
        self.btnCargarReg.clicked.connect(self.mostrar_info)
        
        self.lblID = QLabel("ID") 
        self.lblIDDato = QLabel("...")
        self.lblPrecio = QLabel("Precio") 
        self.lblPreciodato = QLabel("...")
        self.lblTotal = QLabel("Total") 
        self.lblTotalDato = QLabel("...")

        self.grid = QGridLayout() 
        self.grid.addWidget(self.lblnumorden, 1, 0)
        self.grid.addWidget(self.lblOrdennum, 1, 1)     
        self.grid.addWidget(self.lblCliente, 2, 0)     
        self.grid.addWidget(self.lblCli, 2, 1)
        self.grid.addWidget(self.lblsep, 3, 0)
        self.grid.addWidget(self.lblSeccion, 4, 0)     
        self.grid.addWidget(self.ListaSecc, 4, 1)
        self.grid.addWidget(self.lblID, 4, 2) 
        self.grid.addWidget(self.lblIDDato, 4, 3) 
        self.grid.addWidget(self.lblSeccion2, 5, 0)     
        self.grid.addWidget(self.ListaCat, 5, 1) 
        self.grid.addWidget(self.lblPrecio, 5, 2)
        self.grid.addWidget(self.lblPreciodato, 5, 3)
        self.grid.addWidget(self.lblSeccion3, 6, 0)     
        self.grid.addWidget(self.ListaCat2, 6, 1)
        self.grid.addWidget(self.lblCantidad, 7, 0)
        self.grid.addWidget(self.ListaCantidad, 7, 1)
        self.grid.addWidget(self.lblTotal, 7, 2)
        self.grid.addWidget(self.lblTotalDato, 7, 3)
        self.grid.addWidget(self.lblSeparador, 8, 0)
        self.grid.addWidget(self.btnAgregarDato, 9, 0) 
        self.grid.addWidget(self.btnEliminarDato, 9, 1)
        self.grid.addWidget(self.btnModificarReg, 9, 2) 
        self.grid.addWidget(self.btnCargarReg, 9, 3)
        layout.addLayout(self.grid)    

        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(['Id', 'creandola'])                
        self.table.setAlternatingRowColors(True)        
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection) 
        self.table.setColumnHidden(0,True)                            
        layout.setAlignment(Qt.AlignTop)
        layout.addWidget(self.table)        

        self.btnNuevo = QPushButton('Finalizar Orden')
        self.btnNuevo.clicked.connect(self.mostrar_info) 
        self.btnConsultar = QPushButton('Nuevo Cliente')
        self.btnConsultar.clicked.connect(self.mostrar_info) 
        self.btnSalir = QPushButton('Cancelar')
        self.btnSalir.clicked.connect(self.close) 
        GridBotnes = QGridLayout() 
        GridBotnes.addWidget(self.btnNuevo, 0, 0)
        # GridBotnes.addWidget(self.btnConsultar, 0, 1)
        GridBotnes.addWidget(self.btnSalir, 0, 2)
        layout.addLayout(GridBotnes)
                
        self.setLayout(layout)
        

    def EliminarRegistro(self):
        pass

    def ModificarRegistro(self):
        pass

    def CargarRegistro(self):
        pass

    def AgregarPedido(self):        
        base = Database("DetalleOrden","id_Factura","ComObeb","id_comobeb","cantidad","Precio","Total")
        # No llegue a realizarlo...
        # base.insert(f"{str(self.OrdenNumero)}",f"{self.ListaSecc.setCurrentText()}",f"{self.lblIDDato.text()}",f"{self.ListaCantidad.setCurrentText()}",f"{self.lblPreciodato.text()}",f"{self.lblTotalDato.text()}")                    
        # dialogo = QMessageBox.information(self, "Informacion", "Dato Insertado...")            

    def CambioListaCantidad(self):
        Cantidad = int(self.ListaCantidad.currentText())
        precio = int(self.lblPreciodato.text())
        total = Cantidad * precio
        self.lblTotalDato.setText(f"{total}")
        

    def CambioEstadoRegistro(self):
        if self.ListaSecc.currentText() == "Comidas":
            ListaComida = self.ConsultarListComidas()   
            for LisCom in ListaComida:
                posparentesis = self.ListaCat2.currentText()
                posparentesis2 = posparentesis.find(")")
                idcom = int(LisCom[0])
                idboxcom = int(posparentesis[:posparentesis2])
                if idcom == idboxcom:
                    self.lblIDDato.setText(f"{LisCom[0]}")
                    self.lblPreciodato.setText(f"{LisCom[4]}")
        elif self.ListaSecc.currentText() == "Bebidas":
            listabebidas = self.ConsultarListBebidas()            
            for LisBeb in listabebidas:
                posparentesis = self.ListaCat2.currentText()
                posparentesis2 = posparentesis.find(")")
                idcom = int(LisBeb[0])
                idboxcom = int(posparentesis[:posparentesis2])
                if idcom == idboxcom:
                    self.lblIDDato.setText(f"{LisBeb[0]}")
                    self.lblPreciodato.setText(f"{LisBeb[2]}")        
                

        elif self.ListaSecc.currentText() == "Bebidas":
            listabebidas = self.ConsultarListBebidas()            
            for LisBeb in listabebidas:
                self.ListaCat2.addItems([f"{LisBeb[0]}) {LisBeb[1]}"])

    def CambioListaSecc(self):
        if self.ListaSecc.currentText() == "Comidas":
            self.ListaCat.clear()
            self.ListaCat2.clear()
            self.ListaCat.addItems(["Pizza", "Milanesa", "Empanadas"])
            self.ListaCat.setEnabled(True)
        elif self.ListaSecc.currentText() == "Bebidas":
            listabebidas = self.ConsultarListBebidas()
            self.ListaCat.clear()
            self.ListaCat.setEnabled(False)
            self.ListaCat2.setEnabled(True)     
            self.ListaCat2.clear()       
            for LisBeb in listabebidas:
                self.ListaCat2.addItems([f"{LisBeb[0]}) {LisBeb[1]}"])

    def CambioMenuSecc(self):
        ListaComida = self.ConsultarListComidas() 
        self.ListaCat2.setEnabled(True)                   
        self.ListaCat2.clear()        
        for LisCom in ListaComida:
            self.ListaCat2.addItems([f"{LisCom[0]}) {LisCom[2]}"])    
    
    def ConsultarListComidas(self):
        base = Database("Comidas","Categoria","Nombre","Descripcion","Precio")
        ListaComidas = base.selectBuscarComidas("Categoria",self.ListaCat.currentText())        
        return ListaComidas
    
    def ConsultarListBebidas(self):
        base = Database("Bebidas","Marca","Precio")
        Bebidas = base.select() 
        return Bebidas

    def ObtenerNumOrden(self):
        base = Database("OrdenFac","idcliente","Total")
        NumOrden = base.ObtenerUltimoRegistro()
        return NumOrden

    def insertarDatos(self):        
        base = Database("Bebidas","Marca","Precio")       
        if (self.txtMarc.text() == "") or (self.txtPrecio.text() == ""):
            dialogo = QMessageBox.information(self, "Informacion", "Faltan ingresar datos")
        else:
            base.insert(f"{self.txtMarc.text()}",f"{self.txtPrecio.text()}")        
            self.CargarGrillaDatos()
            dialogo = QMessageBox.information(self, "Informacion", "Dato Insertado...")
            self.NuevoDato()
        
    def mostrar_info(self):
        dialogo = QMessageBox.information(
            self, "Informacion", "Lo siento, Creandola...")  