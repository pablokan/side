from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

class SecondaryWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        boton = QPushButton(f"Botón {ventanaPrincipal.entrada.text()}")
        boton.clicked.connect(self.algo)
        layout.addWidget(boton)
        self.setLayout(layout)

    def algo(self):
        ventanaPrincipal.entrada.setText("apreté el botón en la otra ventana")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.entrada = QLineEdit()
        layout.addWidget(self.entrada)
        boton = QPushButton('Abre otra ventana')
        layout.addWidget(boton)
        boton.clicked.connect(self.abrirVentana)
        
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def abrirVentana(self):
        self.ventanaSecundaria = SecondaryWindow()
        self.ventanaSecundaria.show()        

if __name__ == '__main__':
    app = QApplication()
    css = '*{font-size: 50px; background-color: #c6f5c7; color: #850a30;}'
    app.setStyleSheet(css)
    ventanaPrincipal = MainWindow()
    ventanaPrincipal.show()
    app.exec()
