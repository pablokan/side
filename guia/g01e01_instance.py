from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        def instance(lay, clase):
            """
            una función para hacer los dos pasos:
            1) instanciar
            2) colocar en el layout
            en uno solo
            """
            v = clase # instancia
            lay.addWidget(v) # agrega al layout
            return v # devuelve el objeto

        layout = QVBoxLayout()

        self.n1 = instance(layout, QLineEdit())
        self.n2 = instance(layout, QLineEdit())
        boton = instance(layout, QPushButton("Sumar"))
        boton.clicked.connect(self.sumar)
        self.t = instance(layout, QLabel("Resultado"))
        
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
