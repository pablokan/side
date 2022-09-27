from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QLineEdit, 
    QVBoxLayout, 
    QWidget, 
    QLabel,
    QPushButton
    )

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        texto = QLabel("Nombre")
        layout.addWidget(texto)
        cajaTexto = self.cajaTexto = QLineEdit()
        layout.addWidget(cajaTexto)
        boton = QPushButton("Obtener entero")
        layout.addWidget(boton)
        boton.clicked.connect(self.obtener)
        mainContainer = QWidget()
        mainContainer.setLayout(layout)
        self.setCentralWidget(mainContainer)

    def obtener(self):
        numero = int(self.cajaTexto.text())
        print(numero, type(numero))

app = QApplication()
window = Window()
window.show()
app.exec()
