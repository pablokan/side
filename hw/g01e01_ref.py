from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.n1 = QLineEdit()
        layout.addWidget(self.n1)
        self.n2 = QLineEdit()
        layout.addWidget(self.n2)
        boton = QPushButton("Sumar")
        layout.addWidget(boton)
        self.t = QLabel("Resultado")
        layout.addWidget(self.t)

        boton.clicked.connect(self.sumar)
   
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def sumar(self):
        n1 = int(self.n1.text())
        n2 = int(self.n2.text())
        self.t.setText(f"Resultado = {str(n1+n2)}")

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
