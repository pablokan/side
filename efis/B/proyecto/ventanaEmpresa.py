from styles import *
from dataBaseTarifas import actualizarTarifa, traerDatosTarifas
from databaseViajes import traerGanancia

def agregarOpcion(lista, opcion):
    lista.addItems([opcion])

def agregarGama(lista):
    agregarOpcion(lista, 'Elija una opcion')
    agregarOpcion(lista, 'Baja')
    agregarOpcion(lista, 'Media')
    agregarOpcion(lista, 'Alta')

def puntoCadaTres(numero: str):
    nuevoNumero = str()
    numero = numero[::-1]
    for i in range(len(numero)):
        if i % 3 == 0 and i != 0:
            nuevoNumero += "."
        nuevoNumero += numero[i]
    nuevoNumero = nuevoNumero[::-1]
    return nuevoNumero

class WindowEmpresa(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nosotros")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.cajaGama = QGridLayout()
        self.listaDeGama = QComboBox()
        self.layout2 = QFormLayout()
        self.listaDeTarifas = QComboBox()
        
        
        botonInfoEmpresa = Button("Informacion Sobre la Empresa", backg= "#3C6997",fontF= "Arial")
        botonInfoEmpresa.setDefault(True) 
        self.layout.addWidget(botonInfoEmpresa)
        botonInfoEmpresa.clicked.connect(self.infoDeLaEmpresa)
    
        botonInfoTarifa = Button("Informacion Sobre Tarifas", backg= "#3C6997",fontF= "Arial")
        botonInfoTarifa.setDefault(True) 
        self.layout.addWidget(botonInfoTarifa)
        botonInfoTarifa.clicked.connect(self.informacionDeLaTarifa) 

        botonModificarTarifa = Button("ModificarTarifas", backg= "#3C6997",fontF= "Arial")
        botonModificarTarifa.setDefault(True) 
        self.layout.addWidget(botonModificarTarifa)
        botonModificarTarifa.clicked.connect(self.modificacionDeLaTarifa) 

        botonMostrarGanancias = Button("Ganancias Totales", backg= "#3C6997",fontF= "Arial")
        botonMostrarGanancias.setDefault(True) 
        self.layout.addWidget(botonMostrarGanancias)
        botonMostrarGanancias.clicked.connect(self.muestraDeLaGanancia)

    def infoDeLaEmpresa(self):
        self.inf = SaberInformacion()
        self.inf.setStyleSheet("background-color: #094074")
        self.inf.show()
    
    def informacionDeLaTarifa(self):
        self.infoT = InformacionTarifas()
        self.infoT.setStyleSheet("background-color: #094074")
        self.infoT.show()

    def modificacionDeLaTarifa(self):
        self.modT = ModificacionTarifa()
        self.modT.setStyleSheet("background-color: #094074")
        self.modT.show()

    def muestraDeLaGanancia(self):
        self.mues = MuestraGanancia()
        self.mues.setStyleSheet("background-color: #094074")
        self.mues.show()

class SaberInformacion(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.layout = QVBoxLayout()
        self.layout2 = QFormLayout()
        dictInfo = {
        'Nombre ': 'Los input S.A',
        'Sucursal': 'Mitre 213',
        'Pais':'Argentina' ,
        'Localidad' : 'Rio Cuarto',
        'Email' : 'LosInput741@gmail.com'
        }
        
        for k,v in dictInfo.items():     
            mostrarTitulo =Text(k,backg= "#3C6997",fontF= "Arial")
            mostrarInfoTitulo =Text(v,backg= "#3C6997",fontF= "Arial")
            self.layout2.addRow(mostrarTitulo, mostrarInfoTitulo)
            self.layout.addLayout(self.layout2)
        self.setLayout(self.layout)
            
class InformacionTarifas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Informacion de Tarifas") 
        self.layout = QVBoxLayout()
        self.cajaGama = QGridLayout()
        self.listaDeGama = QComboBox()
           
        agregarGama(self.listaDeGama)
        self.cajaGama.addWidget(Text('Seleccione la gama del vehiculo:'), 0, 0)
        self.cajaGama.addWidget(self.listaDeGama, 0, 1)
        self.layout.addLayout(self.cajaGama)
        self.listaDeGama.currentTextChanged.connect(self.elegirGama)
        
        self.setLayout(self.layout)
    
    def elegirGama(self,gamaElegida):
        data = traerDatosTarifas()
        
        for date in data:
            if date[1] == gamaElegida:
                mostrarTarifa= Text(f'Gama: {gamaElegida} | Precio:  ${date[2]}', backg= "#3C6997",fontF= "Arial") 
                self.layout.addWidget(mostrarTarifa)
        
class ModificacionTarifa(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modificacion de Tarifas") 
        self.layout = QVBoxLayout()
        self.cajaGama = QGridLayout()
        self.listaDeGama = QComboBox()
        
        agregarGama(self.listaDeGama)
        self.cajaGama.addWidget(Text('Seleccione la tarifa a modificar:'), 0, 0)
        self.cajaGama.addWidget(self.listaDeGama, 0, 1)
        self.layout.addLayout(self.cajaGama)
        self.listaDeGama.currentTextChanged.connect(self.cambioTarifa)
        self.setLayout(self.layout)
                                                                                                                                                           
    def cambioTarifa(self, precioNuevo):
        self.gama = precioNuevo
        self.layout.addWidget(Text(f'la gama elegida es {self.gama}')) 

        preg = Text("Ingrese el Precio Actualizado")
        self.layout.addWidget(preg)
        self.cambio = Input()
        self.layout.addWidget(self.cambio)

        botonDeCambio = Button("Actualizar")
        self.layout.addWidget(botonDeCambio)
        botonDeCambio.clicked.connect(self.nuevaTarifa) 

    def nuevaTarifa(self):
       actualizarTarifa(self.gama, self.cambio.text())

class MuestraGanancia(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ganancias Totales") 
        self.layout = QVBoxLayout()
    
        ganancias = traerGanancia()
        total = int()
        for n in ganancias:
            total += int(n)
        total = puntoCadaTres(str(total))
        info = Text(f"La ganancia total es de ${total}", backg= "#3C6997")
        self.layout.addWidget(info)
        self.setLayout(self.layout)
        
        
if __name__ == '__main__':
    app = QApplication()
    window = WindowEmpresa()
    window.setStyleSheet("background-color: #094074")
    window.show()
    app.exec()