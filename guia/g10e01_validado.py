# variante más estándar
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLineEdit,
    QLabel, QVBoxLayout, 
    QWidget, QLineEdit, QPushButton)
from PySide6.QtGui import QIntValidator

class InputInt(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setValidator(QIntValidator())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sumar dos números") 
        
        layout = QVBoxLayout() # instancio el vertical box
        
        self.texto = QLabel('Ingrese dos números')
        layout.addWidget(self.texto) 
        
        self.n1 = InputInt() 
        layout.addWidget(self.n1)
        self.n2 = InputInt() 
        layout.addWidget(self.n2)

        bSuma = QPushButton('Sumar')
        bSuma.setDefault(True) # para que funcione con Enter
        layout.addWidget(bSuma) # agrego el botón al vertical box
        bSuma.clicked.connect(self.sumar) # SIGNAL: conecto el click con la función saludar

        self.resultado = QLabel("Resultado")
        layout.addWidget(self.resultado)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def sumar(self): # SLOT: se dispara cuando se produce el evento de click del botón
        s = int(self.n1.text()) + int(self.n2.text())
        self.resultado.setText(f"La suma es {s}")

if __name__ == '__main__':
    app = QApplication()
    css = '*{font-size: 20px; background-color: #66e9f4; color: #101550;}'
    app.setStyleSheet(css)
    window = MainWindow()
    window.show()
    app.exec()
