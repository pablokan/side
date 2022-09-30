import os, sys
sys.path.append(os.path.abspath('libs'))

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout
from styles import Text, Input, Button

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.texto = Text("Ingrese dos numeros", fontF="Broadway", fontS=40, fore="cyan", back="magenta")
        layout.addWidget(self.texto)
        
        self.n1 = Input(fontS=40, fore="white", back="black")
        layout.addWidget(self.n1)
        self.n2 = Input(fontS=40, fore="white", back="black")
        layout.addWidget(self.n2)

        boton = Button('Sumar', fontF="Forte", fontS=40, back="yellow")
        layout.addWidget(boton)
        boton.setDefault(True)
        boton.clicked.connect(self.function_name)

        self.resultado = Text("Resultado", fontS=40, fore="red", back="green")
        layout.addWidget(self.resultado)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def function_name(self):
        s = int(self.n1.text()) + int(self.n2.text())
        self.resultado.setText(f"La suma es {s}")

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
