from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.texto = QLabel('Sumar dos números')
        layout.addWidget(self.texto)
        self.n1 = QLineEdit()
        layout.addWidget(self.n1)
        self.n2 = QLineEdit()
        layout.addWidget(self.n2)
        boton = QPushButton('Sumar')
        layout.addWidget(boton)
        boton.clicked.connect(self.suma)
        
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def suma(self):
        
        self.texto.setText(f'Hola {self.entrada.text()}')

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
