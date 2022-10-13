import os, sys
sys.path.append(os.path.abspath('libs'))

from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout)
from styles import Text, Input, Button

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.layout = layout = QVBoxLayout()

        self.texto = Text('Cuántas edades va a cargar?', fontS=30)
        layout.addWidget(self.texto)

        self.entrada = Input(fontS=30)
        layout.addWidget(self.entrada)
        
        self.boton = boton = Button('Cargar', fontS=30)
        layout.addWidget(boton)
        boton.setDefault(True)
        boton.clicked.connect(self.cargar)
        
        self.contador = 0
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def cargar(self):
        self.cantidad = int(self.entrada.text())
        self.texto.setText("Carga de edades")
        self.entrada.deleteLater()
        self.boton.close()
        self.numero = Input()
        self.t = 0
        self.layout.addWidget(self.numero)
        self.b = b = Button("Agregando...")
        b.clicked.connect(self.promediar)
        self.layout.addWidget(b)
    
    def promediar(self):
        self.contador += 1
        self.t += int(self.numero.text())
        self.numero.clear()
        if self.contador == self.cantidad:
            salida = Text(f"El promedio es {self.t//self.cantidad}")
            self.layout.addWidget(salida)
            self.numero.deleteLater()
            self.b.deleteLater()
        # salida = Text(f"El promedio es {t//len(edades)}")
        # self.layout.addWidget(salida)



if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
