from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        esquema = QVBoxLayout()
        cartel1 = QLabel("Cartel 1")
        esquema.addWidget(cartel1)
        boton = QPushButton("Botón")
        esquema.addWidget(boton)
        boton.clicked.connect(self.foo)
        self.cartel2 = QLabel("Cartel 2")
        esquema.addWidget(self.cartel2)

        centralWidget = QWidget()
        centralWidget.setLayout(esquema)
        self.setCentralWidget(centralWidget)

    def foo(self):
        print("foo")
        self.cartel2.setText("apreté el botón")



if __name__ == "__main__":
    aplicacion = QApplication()
    ventana = MainWindow()
    ventana.show()
    aplicacion.exec()

