from styles import *
from ventanaViaje import *
from ventanaEmpresa import *
from ventanaChoferes import *

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Remiseria")
        self.mainLayout = QVBoxLayout()
        
        self.titulo = Text(string="Bienvenido a Empresa de Jhoskin", fontF="Cambria", fontS=20)
        self.mainLayout.addWidget(self.titulo)
        
        self.botonViaje = Button(string="Nuevo Viaje", fontF="Cambria", fontS=20)
        self.mainLayout.addWidget(self.botonViaje)
        self.botonViaje.clicked.connect(self.abrirVentanaViaje)
        
        self.botonEmpresa = Button(string="Empresa", fontF="Cambria", fontS=20)
        self.mainLayout.addWidget(self.botonEmpresa)
        self.botonEmpresa.clicked.connect(self.abrirVentanaEmpresa)
        
        self.botonChoferes = Button(string="Choferes", fontF="Cambria", fontS=20)
        self.mainLayout.addWidget(self.botonChoferes)
        self.botonChoferes.clicked.connect(self.abrirVentanaChoferes)

        centralWidget = QWidget()
        centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(centralWidget)
    
    def abrirVentanaViaje(self):
        self.windowViaje = WindowViaje()
        self.windowViaje.show()

    def abrirVentanaEmpresa(self):
        self.windowEmpresa = WindowEmpresa()
        self.windowEmpresa.show()
    
    def abrirVentanaChoferes(self):
        self.windowChoferes = WindowChoferes()
        self.windowChoferes.show()
    
if __name__ == '__main__':
    app = QApplication()
    window = VentanaPrincipal()
    window.setStyleSheet("background-color: darkgray")
    window.show()
    app.exec()