from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        qssFiles = ["AMOLED", "Aqua", "ConsoleStyle", "ElegantDark", "MacOS", "ManjaroMix", "MaterialDark", "NeonButtons"]
        with open(f'QSS-master/{qssFiles[7]}.qss', 'r', encoding='utf-8') as file:
            sts = file.read()
        self.setStyleSheet(sts)
        
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
        self.texto.setText(f'Hola {self.entrada.text()}')

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
