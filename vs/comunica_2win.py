# Ejemplo de envío de data ida y vuelta entre ventanas

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.boton = QPushButton(f"Botón {window.entrada.text()}")
        self.entrada = QLineEdit()
        self.boton.clicked.connect(self.vuelta)
        self.boton.setStyleSheet("margin: 30px;")
        layout.addWidget(self.boton)
        layout.addWidget(self.entrada)
        self.setLayout(layout)

    def vuelta(self):
        window.texto.setText(self.entrada.text())
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.texto = QLabel('label')
        layout.addWidget(self.texto)
        self.entrada = QLineEdit()
        layout.addWidget(self.entrada)
        boton = QPushButton('label')
        boton.setDefault(True)
        layout.addWidget(boton)
        boton.clicked.connect(self.function_name)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def function_name(self):
        self.w = Window()
        css = '*{font-size: 30px; background-color: #c6f5c7; color: #850a30;}'
        self.w.setStyleSheet(css)
        self.w.move(3000,200)
        self.w.show()

if __name__ == '__main__':
    app = QApplication()
    css = '*{font-size: 30px; background-color: darkblue; color: skyblue;}'
    window = MainWindow()
    window.setStyleSheet(css)
    window.show()
    app.exec()
