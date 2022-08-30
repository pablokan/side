from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
import sys


class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # empezamos creando un layout vertical
        layout = QVBoxLayout() # QHBoxLayout (para horizontal)

        # le añadimos una caja verde
        layout.addWidget(Caja("green"))
        # le añadimos unas cuantas cajas
        layout.addWidget(Caja("blue"))
        layout.addWidget(Caja("red"))

        # modificamos los márgenes (izq, arr, der, aba)
        layout.setContentsMargins(10,10,0,0)

        # modificamos el espaciado
        layout.setSpacing(10)
    
        # creamos un dummy widget para hacer de contenedor
        widget = QWidget()

        # le asignamos el layout
        widget.setLayout(layout)

        # establecemos el dummy widget como widget central
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
