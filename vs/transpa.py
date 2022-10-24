from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

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
    app = QApplication()
    css = '*{font-size: 40px; background-color:red}'
    app.setStyleSheet(css)
    window = MainWindow()
    css = """
            background-color: yellow;
            background:transparent;
        """
    #window.setWindowFlags(Qt.FramelessWindowHint)
    #window.setAttribute(Qt.WA_TranslucentBackground)
    #window.setStyleSheet(css)
    window.setWindowOpacity(0.75)

    window.show()
    app.exec()
