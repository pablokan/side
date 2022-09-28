from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

cssk = """
QLineEdit, QPushButton, QLabel {
  color: red;
  selection-color: blue;
  selection-background-color: yellow;
  font-family: NovaMono;
  font-size: 70px;
  font-style: italic;
  font-weight: bold;
  text-align: right;
}
"""

class Contenedor(QLabel):
    def __init__(self, color, texto = "texto"):
        super().__init__()
        self.setText("pablokan")
        self.setStyleSheet(cssk)

# font-family, font-size,
#font-style, and/or fontweight

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        caja = Contenedor("green", "kan")
        self.setCentralWidget(caja)


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()