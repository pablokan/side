from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

import qtvscodestyle as qtvsc

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
        self.texto.setText(f'Hola {self.entrada.text()}')

if __name__ == '__main__':
    print(qtvsc.list_themes())
    app = QApplication()
    window = MainWindow()

    stylesheet = qtvsc.load_stylesheet(qtvsc.Theme.DARK_VS)
    stylesheet = qtvsc.load_stylesheet(qtvsc.Theme.KIMBIE_DARK)
    
    theme_file = "pruebas/themes/kimbie.json"
    stylesheet = qtvsc.load_stylesheet(theme_file)
    #stylesheet = qtvsc.load_stylesheet(qtvsc.Theme.SOLARIZED_LIGHT)
    app.setStyleSheet(stylesheet)

    window.show()
    app.exec()
