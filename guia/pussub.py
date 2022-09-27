from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QHBoxLayout, QListWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.nombres = QListWidget()
        layout.addWidget(self.nombres)
        self.sueldos = QListWidget()
        layout.addWidget(self.sueldos)
        self.setLayout(layout)

    def setDato(self, dato):
        self.edito.setText(dato)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.otra = Window()
        layout = QVBoxLayout()
        self.texto = QLabel('label')
        layout.addWidget(self.texto)
        self.entrada = QLineEdit()
        layout.addWidget(self.entrada)
        boton = QPushButton('label')
        layout.addWidget(boton)
        boton.clicked.connect(self.function_name)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def function_name(self):
        self.texto.setText(f'Hola {self.entrada.text()}')
        self.otra.show()
        self.otra.setDato(self.entrada.text())

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
