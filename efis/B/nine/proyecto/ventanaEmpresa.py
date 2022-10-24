from styles import *
from dataBaseTarifas import *

def agregarOpcion(lista, opcion):
    lista.addItems([opcion])

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
        
        botonInfoEmpresa = Button("Informacion Sobre la Empresa", backg= "#D6FFB7",fontF= "Kristen ITC")
        botonInfoEmpresa.setDefault(True) 
        self.layout.addWidget(botonInfoEmpresa)
        botonInfoEmpresa.clicked.connect(self.saberInfoEmpresa)
    
        botonInfoTarifa = Button("Informacion Sobre Tarifas", backg= "#D6FFB7",fontF= "Kristen ITC")
        botonInfoTarifa.setDefault(True) 
        self.layout.addWidget(botonInfoTarifa)
        botonInfoTarifa.clicked.connect(self.infoTarifas) 

        botonModificarTarifa = Button("ModificarTarifas", backg= "#D6FFB7",fontF= "Kristen ITC")
        botonModificarTarifa.setDefault(True) 
        self.layout.addWidget(botonModificarTarifa)
        botonModificarTarifa.clicked.connect(self.modificarTarifa) 


    def saberInfoEmpresa(self):
        dictInfo = {'Nombre ': 'Los input S.A', 'Sucursal': 'Mitre 213','Pais':'Argentina' ,'Localidad' : 'Rio Cuarto', 'Email' : 'LosInput741@gmail.com',}
        for k,v in dictInfo.items():
            mostrarTitulo =Text(k,backg= "#D6FFB7",fontF= "Kristen ITC")
            mostrarInfoTitulo =Text(v,backg= "#D6FFB7",fontF= "Kristen ITC")
            self.layout2.addRow(mostrarTitulo, mostrarInfoTitulo)
            self.layout.addLayout(self.layout2)
        
    def infoTarifas(self):
        agregarOpcion(self.listaDeGama, 'Elija una opcion')
        agregarOpcion(self.listaDeGama, 'Baja')
        agregarOpcion(self.listaDeGama, 'Media')
        agregarOpcion(self.listaDeGama, 'Alta')

        self.cajaGama.addWidget(Text('Seleccione la gama del vehiculo:'), 0, 0)
        self.cajaGama.addWidget(self.listaDeGama, 0, 1)
        self.layout.addLayout(self.cajaGama)
        self.listaDeGama.currentTextChanged.connect(self.elegirGama)
        self.setLayout(self.layout)

    def elegirGama(self,gamaElegida):
        #sacar el parametro'gamaElegida' se cambia por self.sender().text()
        data = tarifas.select()
        for date in data:
            if date[1] == gamaElegida:
                mostrarTarifa=Text(f'La gama elegida es {gamaElegida}, el precio por km es ${date[2]}', backg= "#D6FFB7",fontF= "Kristen ITC") 
                self.layout.addWidget(mostrarTarifa)

    def modificarTarifa(self):
        agregarOpcion(self.listaDeTarifas, 'Elija una opcion')
        agregarOpcion(self.listaDeTarifas, 'Baja')
        agregarOpcion(self.listaDeTarifas, 'Media')
        agregarOpcion(self.listaDeTarifas, 'Alta')

        self.cajaGama.addWidget(Text('Seleccione la tarifa a modificar:'), 0, 0)
        self.cajaGama.addWidget(self.listaDeTarifas, 0, 1)
        self.layout.addLayout(self.cajaGama)
        self.listaDeTarifas.currentTextChanged.connect(self.cambioTarifa)
        
                                                                                                                                                   
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

    def guardarTarifaNueva(self):
        pass
        # definirTarifas(self.gama, self.cambio)
        

if __name__ == '__main__':
    app = QApplication()
    window = WindowEmpresa()
    window.setStyleSheet("background-color: #C1DF1F")
    window.show()
    app.exec()
