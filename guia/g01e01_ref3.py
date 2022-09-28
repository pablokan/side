from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        def instance(lay, clase):
            v = clase
            lay.addWidget(v)
            return v

        layout = QVBoxLayout()

        self.n1 = instance(layout, QLineEdit())
        self.n2 = instance(layout, QLineEdit())
        boton = instance(layout, QPushButton("Sumar"))
        self.t = instance(layout, QLabel("Resultado"))

        boton.clicked.connect(self.sumar)
   
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def sumar(self):
        n1 = int(self.n1.text())
        n2 = int(self.n2.text())
        self.t.setText(f"Resultado = {str(n1+n2)}")

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
