from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit
import sys


class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # layout vertical
        layout = QVBoxLayout() # QHBoxLayout (para horizontal)

        i = self.i = QLineEdit()
        layout.addWidget(i)
        t = self.t = QLabel("holis")
        self.i.returnPressed.connect(self.enter_presionado)
        layout.addWidget(t)
   
        # creamos un dummy widget para hacer de contenedor
        widget = QWidget()

        # le asignamos el layout
        widget.setLayout(layout)

        # establecemos el dummy widget como widget central
        self.setCentralWidget(widget)

    def enter_presionado(self):
        self.t.setText(self.i.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
