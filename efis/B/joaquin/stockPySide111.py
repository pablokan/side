from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
QPushButton, QFormLayout, QLineEdit, QComboBox,QTableWidget, QTableWidgetItem) 
from PySide6.QtGui import QIntValidator
from qt_material import apply_stylesheet
from database import Database

baseCat = Database("Categorias","Nombre","StockCria","StockInvernada","StockTotal") # Ver cual es el mejor lugar para generarlo

class SubventanaAddCategory(QWidget): # Para Boton de agregar una categoria.
    def __init__(self):
        super().__init__()
        self.resize(350, 120)
        self.setWindowTitle("Agregar categoría")

        principal = QVBoxLayout() #Defino el vertical que va a actuar de principal.
        self.setLayout(principal) # Necesario para que el principal quede configurado en el Qwidget que es la clase padre.
        
        self.QFlayout = QFormLayout()
        principal.addLayout(self.QFlayout)

        self.entrada = QLineEdit()
        self.entrada.setClearButtonEnabled(True)     

        self.QFlayout.addRow("Nombre de categoria nueva: ", self.entrada)

        botonAddCategoria = QPushButton("Confirmar")
        principal.addWidget(botonAddCategoria)  
        botonAddCategoria.clicked.connect(self.apCategoria)    

    def apCategoria(self):
        nombre = self.entrada.text()
        baseCat.insert(nombre,0,0,0)
        id = baseCat.select()[-1][0] # El ultimo agregado. Lo hago para no tener que salir y volver a entrar.
        for actividad in c.actividades:
            actividad.detalle.append(Animal(id,nombre))

class SubventanaAddStock(QWidget): # Para Boton de agregar Cria o Invernada.
    def __init__(self):
        super().__init__()
        self.resize(350, 120)
        self.setWindowTitle(f"Agregar stock {c.nombre_empresa}")

        principal = QVBoxLayout() #Defino el vertical que va a actuar de principal.
        self.setLayout(principal) # Necesario para que el principal quede configurado en el Qwidget que es la clase padre.
        
        QFlayout = QFormLayout() # Defino el formulario
        principal.addLayout(QFlayout) # Agrego el formulario al principal
        
        self.desplegableCategoria = QComboBox()  # Defino desplegable que va a ir en formulario  
        lCat = [elemento[1] for elemento in baseCat.select()]
        for cat in lCat:
            self.desplegableCategoria.addItem(cat)
        
        self.desplegableActividades = QComboBox() # Desplegable que contiene nombre de actividades.
        lAct = [elemento[1] for elemento in c.nombreAct]
        for act in lAct:
            self.desplegableActividades.addItem(act)

        self.cantStock = QLineEdit() # Defino editable que va a ir en formulario
        validador = QIntValidator()
        self.cantStock.setValidator(validador)
        self.cantStock.setClearButtonEnabled(True)
        label1 = QLabel("Agregar datos")

        #Agrego filas al formulario.
        QFlayout.addRow(label1) 
        QFlayout.addRow("Actividad: ",self.desplegableActividades)
        QFlayout.addRow("Categoria: ", self.desplegableCategoria)
        QFlayout.addRow("Cantidad: ", self.cantStock)
        
        # Defino en el principal el boton que confirma la operacion
        botonAddStock = QPushButton("Confirmar")
        principal.addWidget(botonAddStock)
        botonAddStock.clicked.connect(self.confStock)
        
    def confStock(self):
        # Busco la categoria que cargue y la posicion que ocupa en lista de categorias (Objeto Animales)
        self.lCat = [elemento[1] for elemento in baseCat.select()]
        self.lId = [(elemento[1], elemento[0]) for elemento in baseCat.select()]
        categoria = self.desplegableCategoria.currentText() 
        posCat = 0
        for i in self.lId:
            if categoria == i[0]:
                posCat = i[1] # Va a devolver la fila de la categoria en la base de datos.
        cantidad = int(self.cantStock.text())
        # Busco la actividad que cargue y la posicion que ocupa en lista de actividades (Objeto Actividades)
        self.lAct = [elemento.nombre for elemento in c.actividades]
        self.lIdAct = [(elemento[1], elemento[0]) for elemento in c.nombreAct]
        activ = self.desplegableActividades.currentText()
        posAct = 0
        for i in self.lIdAct:
            if activ == i[0]:
                posAct = i[1]+2 # Porque devuelve 0,1, pero yo quiero la posicion en base que es 2,3
        datos = baseCat.select()
        aux = int(datos[posCat][posAct])
        valor = int(datos[posCat][posAct]) + cantidad # Este es el nuevo valor que hay que actualizar en la base.
        if activ == "Cria":
            valorTotal = int(datos[posCat][4]) + valor - aux
            baseCat.update(datos[posCat][0],datos[posCat][1],valor,datos[posCat][3],valorTotal)
        else:
            valorTotal = int(datos[posCat][4]) + valor - aux
            baseCat.update(datos[posCat][0],datos[posCat][1],datos[posCat][2],valor,valorTotal)
        
class Tabla(QTableWidget): # Tabla que muestra Stock.
    def __init__(self,encabezado):
        super().__init__()
        self.resize(600, 250)
        # Armo estructura de tabla:
        self.setRowCount(len(baseCat.select())) # Agrega filas segun la cantidad de categorias
        self.setColumnCount(len(c.nombreAct)+2) # Agrega columnas segun la cantidad de actividades + Nombre + Total
        self.horizontalHeader().setStretchLastSection(True)
        self.setHorizontalHeaderLabels(encabezado) # Para ponerle titulo a las columnas
        self.setAlternatingRowColors(True) # Colores alternados de filas.
        
        # Carga de datos en tabla:
        # Para categorias
        datos = baseCat.select()
        for fila in range(len(datos)):
            dato = QTableWidgetItem(datos[fila][1])
            self.setItem(fila,0,dato)
        self.resizeColumnsToContents()
        # Para Stocks.
        for fila in range(len(datos)): # fila = posicion de eje en fila
            for columna in range(1,len(c.nombreAct)+2): # Columna = posicion de eje en columna.
                valor = datos[fila][columna+1] # Pongo + 1 porque busco la ubicacion del stock en la tupla de la base.
                dato = QTableWidgetItem(str(valor)) # Convierto para agregar, tiene que estar en str.
                self.setItem(fila,columna,dato) # Agrego
        self.resizeColumnsToContents()

class VentanaPrincipal(QMainWindow):
    def __init__(self,) -> None:
        super().__init__()

        def addbotonFuncion(msj,lay,funcion):
            boton = QPushButton(msj)
            lay.addWidget(boton)
            boton.clicked.connect(funcion)            

        layout = QVBoxLayout()
        self.resize(400, 200)
        #self.setGeometry(400,200,200,200) 

        # Botones principales y su conexion hacia las subventanas

        addbotonFuncion("Agregar Stock",layout,self.addStock)
        addbotonFuncion("Mostrar Stock",layout,self.showStock)
        addbotonFuncion("Agregar Categoría",layout,self.addCat)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    # Metodos que abren subventanas:

    def addStock(self):
        self.subWAddStock = SubventanaAddStock()
        apply_stylesheet(self.subWAddStock,theme= "dark_amber.xml")
        self.subWAddStock.show()

    def addCat(self):
        self.subWAddCategoria = SubventanaAddCategory()
        apply_stylesheet(self.subWAddCategoria,theme= "dark_amber.xml")
        self.subWAddCategoria.show()
    
    def showStock(self):
        self.subWShowStock = Tabla(("Categoria","Cria","Invernada","Total"))
        apply_stylesheet(self.subWShowStock,theme= "dark_amber.xml")
        self.subWShowStock.show()        

class Animal():
    def __init__(self,id,categoria,stock=0) -> None:
        self.id = id
        self.categoria = categoria
        self.stock = stock

    def __repr__(self) -> str:
        return f"{self.categoria} {self.stock}"

class Actividad():
    def __init__(self,nombre,categorias) -> None:
        self.nombre = nombre
        self.detalle = []
        self.categorias = categorias

        for categoria in self.categorias:
            a = Animal(*categoria)
            self.detalle.append(a)

class Campo():
    def __init__(self,nombre_empresa) -> None:
        self.categorias = [(elemento[0],elemento[1]) for elemento in baseCat.select()] 
        self.nombre_empresa = nombre_empresa
        self.actividades = []
        self.nombreAct = [(0,"Cria"),(1,"Invernada")] 
        for i in range(len(self.nombreAct)):
            actividad = Actividad(self.nombreAct[i][1],self.categorias)
            self.actividades.append(actividad)

#Prog ppal
app = QApplication()
c = Campo("Quino")
apply_stylesheet(app,theme= "dark_teal.xml")
v = VentanaPrincipal()
v.show()
app.exec()


