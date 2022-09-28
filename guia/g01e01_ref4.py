from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

class KInput(QLineEdit):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")

class KText(QLabel):
    def __init__(self, texto, color):
        super().__init__(texto)
        self.setStyleSheet(f"background-color:{color}")

class KButton(QPushButton):
    def __init__(self, texto, color):
        super().__init__(texto)
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        def instance(lay, clase):
            v = clase
            lay.addWidget(v)
            return v

        layout = QVBoxLayout()

        self.n1 = instance(layout, QLineEdit())
        self.n2 = instance(layout, KInput("teal"))
        boton = instance(layout, KButton("Sumar", "magenta"))
        self.t = instance(layout, KText("Resultado", "red"))

        boton.clicked.connect(self.sumar)
   
        centralWidget = QWidget()
        centralWidget.setStyleSheet(f"background-color: yellow")
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
