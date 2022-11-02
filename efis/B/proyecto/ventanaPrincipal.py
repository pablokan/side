from styles import *
from ventanaViaje import WindowViaje
from ventanaEmpresa import WindowEmpresa
from ventanaChoferes import WindowChoferes

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Remiseria")
        self.mainLayout = QVBoxLayout()
        
        self.titulo = Text(string="Bienvenido a Empresa de viajes")
        self.mainLayout.addWidget(self.titulo)
        
        self.botonViaje = Button(string="Nuevo Viaje")
        self.mainLayout.addWidget(self.botonViaje)
        self.botonViaje.clicked.connect(self.abrirVentanaViaje)
        
        self.botonEmpresa = Button(string="Empresa")
        self.mainLayout.addWidget(self.botonEmpresa)
        self.botonEmpresa.clicked.connect(self.abrirVentanaEmpresa)
        
        self.botonChoferes = Button(string="Choferes")
        self.mainLayout.addWidget(self.botonChoferes)
        self.botonChoferes.clicked.connect(self.abrirVentanaChoferes)

        centralWidget = QWidget()
        centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(centralWidget)
    
    def abrirVentanaViaje(self):
        self.windowViaje = WindowViaje()
        self.windowViaje.setStyleSheet("background-color: #094074")

        self.windowViaje.show()

    def abrirVentanaEmpresa(self):
        self.windowEmpresa = WindowEmpresa()
        self.windowEmpresa.setStyleSheet("background-color: #094074")

        self.windowEmpresa.show()
    
    def abrirVentanaChoferes(self):
        self.windowChoferes = WindowChoferes()
        self.windowChoferes.setGeometry(700,70,250,150)
        self.windowChoferes.setStyleSheet("background-color: #094074")
        self.windowChoferes.show()
    
if __name__ == '__main__':
    app = QApplication()
    window = VentanaPrincipal()
    window.setStyleSheet("background-color: #094074")
    window.show()
    app.exec()