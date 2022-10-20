from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        boton = QPushButton(f"Botón {ventanaPrincipal.entrada.text()}")
        boton.clicked.connect(self.algo)
        layout.addWidget(boton)
        
        self.setLayout(layout)

    def algo(self):
        print('algo')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.entrada = QLineEdit()
        layout.addWidget(self.entrada)
        boton = QPushButton('Allá va!')
        layout.addWidget(boton)
        boton.clicked.connect(self.abrirVentana)
        
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def abrirVentana(self):
        self.ventanita = Window()
        self.ventanita.show()

if __name__ == '__main__':
    app = QApplication()
    css = '*{font-size: 30px; background-color: darkblue; color: skyblue;}'
    app.setStyleSheet(css)
    ventanaPrincipal = MainWindow()
    ventanaPrincipal.show()
    app.exec()
