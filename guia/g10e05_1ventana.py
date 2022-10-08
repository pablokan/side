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
        
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def cargar(self):
        cantidad = int(self.entrada.text())
        self.texto.setText("Carga de edades")
        self.entrada.deleteLater()
        self.boton.close()
        for _ in range(cantidad):
            self.layout.addWidget(Input())
        b = Button("Promediar")
        b.clicked.connect(self.promediar)
        self.layout.addWidget(b)
    
    def promediar(self):
        t = 0
        edades = self.findChildren(Input)
        for edad in edades:
            t += int(edad.text())
        salida = Text(f"El promedio es {t//len(edades)}")
        self.layout.addWidget(salida)



if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
