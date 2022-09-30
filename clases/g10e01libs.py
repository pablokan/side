import os, sys
sys.path.append(os.path.abspath('libs'))

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout
from styles0 import Text, Input, Button

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.texto = Text('Ingrese 2 números', fontF="NovaMono", fontS=30, fore="red", back="yellow")
        layout.addWidget(self.texto)
        self.numero1 = Input(fontS=40, fore="magenta", back="black")
        layout.addWidget(self.numero1)
        self.numero2 = Input(fontS=40, fore="magenta", back="black")
        layout.addWidget(self.numero2)
        boton = Button('Sumar', back="orange", fontF="Chiller", fontS=50)
        layout.addWidget(boton)
        self.resultado = Text(fontS=60)
        layout.addWidget(self.resultado)
        boton.setDefault(True)
        boton.clicked.connect(self.sumar)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def sumar(self): # SLOT: se dispara cuando se produce el evento de click del botón
        n1 = int(self.numero1.text())
        n2 = int(self.numero2.text())
        suma = str(n1 + n2)
        self.resultado.setText(f"La suma es {suma}")

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
