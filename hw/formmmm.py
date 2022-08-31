from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QFormLayout, QWidget, QLineEdit)
import sys


class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un layout en formulario
        formulario = QFormLayout()

        # añadimos widgets con etiquetas en filas
        formulario.addRow("Campo 1", Caja("orange"))
        formulario.addRow("Campo 2", Caja("purple"))
        formulario.addRow("Campo 3", QLineEdit())
        formulario.addRow("Campo 4", Caja("gray"))
        formulario.addRow("Campo 5", Caja("red"))

        # cremos el widget dummy y le asignamos el layout
        widget = QWidget()
        widget.setLayout(formulario)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
