from styles import *
from databaseChoferes import agregar, eliminar, traerDatos

class WindowChoferes(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choferes")
        self.layout = QVBoxLayout()
        
        botonAgregar = Button(string="Agregar Empleado", fontF="Cambria", fontS=18)
        self.layout.addWidget(botonAgregar)
        botonAgregar.clicked.connect(self.agregarEmpleado)
        
        botonEliminar = Button(string="Eliminar Empleado", fontF="Cambria", fontS=18)
        self.layout.addWidget(botonEliminar)
        botonEliminar.clicked.connect(self.eliminarEmpleado)
        
        botonMostrarChoferes = Button(string="Mostrar Choferes", fontF="Cambria", fontS=18)
        self.layout.addWidget(botonMostrarChoferes)
        botonMostrarChoferes.clicked.connect(self.mostrarChoferes)
               
        self.setLayout(self.layout)
        
    def agregarEmpleado(self):
        self.agg = AgregarChoferes()
        self.agg.show()

    def eliminarEmpleado(self):
        self.eliminar = EliminarEmpleado()
        self.eliminar.show()
        
    def mostrarChoferes(self):
        self.mostrar = MostrarEmpleados()
        self.mostrar.show()
            
class AgregarChoferes(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.formulario = QFormLayout()
        preg = Text(string="Ingrese los datos del empleado")
        self.layout.addWidget(preg)
        self.formulario.addRow(Text(string="Ingrese nombre"), Input())#set.Validator(QIntValidator)
        self.formulario.addRow(Text(string="Ingrese DNI"), Input())
        self.layout.addLayout(self.formulario)
        botones = QGridLayout()
        bg = QButtonGroup(self)
        baja = QRadioButton("Baja", self)
        media = QRadioButton("Media", self)
        alta = QRadioButton("Alta", self)
        botones.addWidget(Text(string="Gama de auto: "), 0, 0)
        botones.addWidget(baja, 0, 1)
        botones.addWidget(media, 0, 2)
        botones.addWidget(alta, 0, 3)
        bg.addButton(baja)
        bg.addButton(media)
        bg.addButton(alta)
        self.layout.addLayout(botones)
        botonParaPasar = Button("Cargar empleado", fontF="Cambria") 
        self.layout.addWidget(botonParaPasar)
        botonParaPasar.clicked.connect(self.pasarDatos)

        self.setLayout(self.layout)

    def pasarDatos(self):
        datos = self.findChildren(Input)
        gama = self.findChildren(QButtonGroup)
        print(gama[0].checkedId())
        if gama[0].checkedId() == -4:
            agregar(datos[0].text(), datos[1].text(), "alta")
        elif gama[0].checkedId() == -3:
            agregar(datos[0].text(), datos[1].text(), "media")
        elif gama[0].checkedId() == -2:
            agregar(datos[0].text(), datos[1].text(), "baja")    

class EliminarEmpleado(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        preg = Text(string="Ingrese el nombre del empleado a eliminar")
        self.layout.addWidget(preg)
        self.nombre = Input()
        self.layout.addWidget(self.nombre)
        botonNombre = Button("Eliminar empleado")
        self.layout.addWidget(botonNombre)
        botonNombre.clicked.connect(self.eliminarEmp)
        self.setLayout(self.layout)
    
    def eliminarEmp(self):
        eliminar(self.nombre.text())

class MostrarEmpleados(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QFormLayout()
        nombres = traerDatos("nombres")
        gamas = traerDatos("gama")
        self.layout.addRow(Text("Chofer"), Text("Gama"))
        for i in range(len(nombres)):
            self.layout.addRow(Text(f"{nombres[i]}"), Text(f"{gamas[i]}"))
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication()
    window = WindowChoferes()
    window.show()
    app.exec()
    
        
