from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QFormLayout, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mainLayout = QVBoxLayout()
        formulario = QFormLayout()
        botonera = QHBoxLayout()
        self.nombre = QLineEdit()
        formulario.addRow("Campo 1", self.nombre)
        formulario.addRow("Campo 2", QLineEdit())
        boton = QPushButton("obtener")
        boton.clicked.connect(self.obtener)
        nada = QPushButton("Nada")
        botonera.addWidget(boton)
        botonera.addWidget(nada)
        
        mainLayout.addLayout(formulario)
        mainLayout.addLayout(botonera)
        
        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

    def obtener(self):
        print(self.nombre.text())

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()