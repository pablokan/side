from styles import *
from databaseChoferes import traerDatos
from databaseViajes import agregarViaje
from dataBaseTarifas import *

def agregarOpcion(lista, opcion):
    lista.addItems([opcion])

class WindowViaje(QWidget):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("Viaje")
        
        self.layout = QVBoxLayout()
        cajaGama = QGridLayout()
        listaDeGama = QComboBox()

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
        data = tarifas.select()
        self.precio = ""
        for date in data:
            if date[1] == gamaElegida:
                mostrarTarifa=Text(f'La gama elegida es {gamaElegida}, el precio por km es ${date[2]}', backg= "#D6FFB7",fontF= "Kristen ITC") 
                self.precio = int(date[2])
                self.layout.addWidget(mostrarTarifa)

        cajaChoferes = QGridLayout()
        listaDeChoferes = QComboBox()
        agregarOpcion(listaDeChoferes, 'Elija una opcion')
        
        nombresChoferes = traerDatos("nombres")
        gamaChoferes = traerDatos("gama")
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
        agregarViaje(self.nombreChofer, self.presupuesto, self.distancia)
       
if __name__ == '__main__':
    app = QApplication()
    window = WindowViaje()
    window.show()
    app.exec()