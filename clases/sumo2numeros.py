from PySide6.QtWidgets import (
    QApplication, QMainWindow, 
    QLabel, QVBoxLayout, 
    QWidget, QLineEdit, QPushButton)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sumar dos números") # ya que está le pongo título a la ventana
        layout = QVBoxLayout() # instancio el vertical box
        self.texto = QLabel('Ingrese dos números:') # instancio un texto
        layout.addWidget(self.texto) # agrego el texto al vertical box
        self.n1 = QLineEdit() # instancio una caja de texto
        layout.addWidget(self.n1) # agrego la caja de texto al vertical box
        self.n2 = QLineEdit() # instancio una caja de texto
        layout.addWidget(self.n2) # agrego la caja de texto al vertical box
        boton = QPushButton('Sumar') # instancio un botón
        boton.setDefault(True)
        layout.addWidget(boton) # agrego el botón al vertical box
        boton.clicked.connect(self.sumar) # SIGNAL: conecto el click con la función saludar
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def sumar(self):
        s = int(self.n1.text()) + int(self.n2.text())
        self.texto.setText(str(s)) 

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
