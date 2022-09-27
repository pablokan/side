from PySide6.QtWidgets import (
    QApplication, QMainWindow, 
    QLabel, QVBoxLayout, 
    QWidget, QLineEdit, QPushButton)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Saludo!") # ya que está le pongo título a la ventana
        layout = QVBoxLayout() # instancio el vertical box
        self.texto = QLabel('Ingrese su nombre:') # instancio un texto
        layout.addWidget(self.texto) # agrego el texto al vertical box
        self.entrada = QLineEdit() # instancio una caja de texto
        layout.addWidget(self.entrada) # agrego la caja de texto al vertical box
        boton = QPushButton('Saludar') # instancio un botón
        boton.setDefault(True) # para que funcione con Enter
        layout.addWidget(boton) # agrego el botón al vertical box
        boton.clicked.connect(self.saludar) # SIGNAL: conecto el click con la función saludar
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def saludar(self): # SLOT: se dispara cuando se produce el evento de click del botón
        # .text() es el getter que devuelve el str contenido en el objeto texto
        self.texto.setText(f'Hola {self.entrada.text()}') 

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
