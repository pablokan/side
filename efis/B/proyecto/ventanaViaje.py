from styles import *
from databaseChoferes import traerDatosChoferes
from databaseViajes import agregarViaje
from dataBaseTarifas import traerDatosTarifas

def agregarOpcion(lista, opcion):
    lista.addItems([opcion])

class WindowViaje(QWidget):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("Viaje")
        
        self.layout = QVBoxLayout()
        cajaGama = QGridLayout()
        listaDeGama = QComboBox()        
        listaDeGama.setStyleSheet('QComboBox''{''background-color: #5ADBFF; ''}'
        'QListView''{''background-color: #5ADBFF; ''}')
        


        agregarOpcion(listaDeGama, 'Elija una opcion')
        agregarOpcion(listaDeGama, 'Baja')
        agregarOpcion(listaDeGama, 'Media')
        agregarOpcion(listaDeGama, 'Alta')

        cajaGama.addWidget(Text('Seleccione la gama del vehiculo:'), 0, 0)
        cajaGama.addWidget(listaDeGama, 0, 1)
        self.layout.addLayout(cajaGama)

        listaDeGama.currentTextChanged.connect(self.elegirGama)

        self.setLayout(self.layout)

    def elegirGama(self, gamaElegida):
        #sacar el parametro'gamaElegida' se cambia por self.sender().text()
        data = traerDatosTarifas()
        
        for date in data:
            if date[1] == gamaElegida:
                self.precio = int(date[2])
                mostrarTarifa= Text(f'La gama elegida es {gamaElegida}, el precio por km es ${self.precio}') 

                self.layout.addWidget(mostrarTarifa)

        cajaChoferes = QGridLayout()
        listaDeChoferes = QComboBox()
        agregarOpcion(listaDeChoferes, 'Elija una opcion')
        
        nombresChoferes = traerDatosChoferes("nombres")
        gamaChoferes = traerDatosChoferes("gama")
        for i in range(len(nombresChoferes)):
            if gamaChoferes[i] == gamaElegida.lower():
                agregarOpcion(listaDeChoferes, nombresChoferes[i])

        cajaChoferes.addWidget(Text('Elija su Chofer:'), 0, 0)
        cajaChoferes.addWidget(listaDeChoferes, 0, 1)
        self.layout.addLayout(cajaChoferes)
        listaDeChoferes.currentTextChanged.connect(self.elegirChofer)

    def elegirChofer(self, choferElegido):
        self.nombreChofer = choferElegido 
        self.layout.addWidget(Text(f'El chofer elegido es {self.nombreChofer}')) 
        self.layout.addWidget(Text('Ingrese la distancia que va a recorrer(en km):'))
        self.ingresarDistancia = Input() #validador de numero
        self.layout.addWidget(self.ingresarDistancia)
        
        self.hacerPresupuesto = QPushButton('Presupuestar viaje')
        self.layout.addWidget(self.hacerPresupuesto)
        self.hacerPresupuesto.clicked.connect(self.calcularPresupuesto)

    def calcularPresupuesto(self):
        self.distancia = self.ingresarDistancia.text()
        self.presupuesto = int(self.distancia) * self.precio

        self.layout.addWidget(Text(f'El costo estimado del viaje es de ${self.presupuesto}'))
        aceptarViaje = Button('Aceptar viaje')
        self.layout.addWidget(aceptarViaje)
        aceptarViaje.clicked.connect(self.guardarViaje)
        
    def guardarViaje(self):
        agregarViaje(self.nombreChofer, self.distancia, self.presupuesto)
       
if __name__ == '__main__':
    app = QApplication()
    window = WindowViaje()
    window.show()
    app.exec()