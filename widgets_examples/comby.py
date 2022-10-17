from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QComboBox
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.texto = QLabel('label')
        layout.addWidget(self.texto)
        combo = QComboBox()
        layout.addWidget(combo)
        combo.addItems(["One", "Two", "Three"])
        combo.currentIndexChanged.connect(self.index_changed)
        combo.currentTextChanged.connect(self.text_changed)
        self.entrada = QLineEdit()
        layout.addWidget(self.entrada)
        boton = QPushButton('label')
        boton.setDefault(True)
        layout.addWidget(boton)
        boton.clicked.connect(self.function_name)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def index_changed(self, i): # i is an int
        print(i)
        
    def text_changed(self, s): # s is a str
        print(s)

    def function_name(self):
        self.texto.setText(f'Hola {self.entrada.text()}')

if __name__ == '__main__':
    app = QApplication()
    css = '*{font-size: 20px; background-color: black; color: yellow;}'
    app.setStyleSheet(css)
    window = MainWindow()
    window.show()
    app.exec()
