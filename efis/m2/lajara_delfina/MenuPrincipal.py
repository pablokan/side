from PySide6.QtWidgets import (QApplication, QMainWindow,QMessageBox,QStatusBar,QLabel)
from PySide6.QtGui import QAction, QIcon, QPixmap
from Interfaces.AdmCliente import VentanaCliente
from Interfaces.AdmMenu import VentanaMenuComidas
from Interfaces.AdmBebida import VentanaBebidas
from Interfaces.NewOrden import NewOrden
from pathlib import Path
import sys

def absPath(file):
    return str(Path(__file__).parent.absolute() / file)

class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()        
        self.resize(612, 360)    
        self.setWindowTitle("Menu Principal - Bar Berlin")            
        self.construir_menu()
        self.setStatusBar(QStatusBar(self))

    def construir_menu(self):        
        menu = self.menuBar()        
        menu_archivo = menu.addMenu("&Menú")                
        menu_archivo.addAction(QIcon(absPath("")), "N&ueva Orden", self.Mostrar_VentanaNewOrden, "Ctrl+N")        
        menu_archivo.addSeparator() 
        menu_archivo.addAction(QIcon(absPath("img/Dato1.png")), "A&dm Clientes", self.Mostrar_VentanaCliente, "Ctrl+C")        
        submenu_archivo = menu_archivo.addMenu("&Adm Menu")        
        submenu_archivo.addAction(QIcon(absPath("img/Dato1.png")), "Adm C&omidas", self.Mostrar_VentanaComidas, "Ctrl+M")
        submenu_archivo.addAction(QIcon(absPath("img/Dato1.png")), "Adm B&ebidas", self.Mostrar_VentanaBebidas, "Ctrl+B")        
        menu_archivo.addSeparator()        
        menu_archivo.addAction(QIcon(absPath("exit.png")), "S&alir", self.close, "Ctrl+Q")        
        menu_ayuda = menu.addMenu("Ay&uda")        
        accion_info = QAction("&Información", self)        
        accion_info.setIcon(QIcon(absPath("info.png")))        
        accion_info.setShortcut("Ctrl+I")        
        accion_info.triggered.connect(self.mostrar_info)        
        accion_info.setStatusTip("Muestra información irrelevante")        
        menu_ayuda.addAction(accion_info)        
        Fondo = QLabel("Soy una etiqueta")        
        self.setCentralWidget(Fondo)
        imagen = QPixmap("img\FondoPrincipal.jpg")        
        Fondo.setPixmap(imagen)        
                
    def Mostrar_VentanaCliente(self):
        self.subventana = VentanaCliente()
        self.subventana.show()

    def Mostrar_VentanaComidas(self):
        self.subventana = VentanaMenuComidas()
        self.subventana.show()

    def Mostrar_VentanaBebidas(self):
        self.subventana = VentanaBebidas()
        self.subventana.show()

    def Mostrar_VentanaNewOrden(self):        
        self.subventana = NewOrden()
        self.subventana.show()

    def mostrar_info(self):
        dialogo = QMessageBox.information(self, "Informacion", "Bar - Berlin")

    def mostrar_info2(self):
        dialogo = QMessageBox.information(self, "Informacion", "Lo siento. Creandola...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuPrincipal()
    window.show()
    sys.exit(app.exec())