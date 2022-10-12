from PySide6.QtWidgets import (
    QApplication, QMainWindow, 
    QLabel, QVBoxLayout, 
    QWidget, QLineEdit, QPushButton)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contar vocales") # ya que está le pongo título a la ventana
        layout = QVBoxLayout() # instancio el vertical box
        self.texto = QLabel('Ingrese una frase') # instancio un texto
        layout.addWidget(self.texto) # agrego el texto al vertical box
        self.entrada = QLineEdit() # instancio una caja de texto
        layout.addWidget(self.entrada) # agrego la caja de texto al vertical box
        boton = QPushButton('Contar vocales') # instancio un botón
        layout.addWidget(boton) # agrego el botón al vertical box
        boton.clicked.connect(self.contar) # SIGNAL: conecto el click con la función saludar
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def contar(self):
        c = 0
        for letra in self.entrada.text():
            if letra in "aeiou":
                c += 1
        self.texto.setText(f"Hay {c} vocales") 

if __name__ == '__main__':
    app = QApplication()
    css = '*{font-size: 20px; background-color: #277c2c; color: #f4fc6b;}'
    app.setStyleSheet(css)
    window = MainWindow()
    window.show()
    app.exec()
