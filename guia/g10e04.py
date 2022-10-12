# Pedir el ingreso de 10 números. Contar los mayores de 23.

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QWidget, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        def instance(lay, clase):
            v = clase
            lay.addWidget(v)
            return v

        layout = QHBoxLayout()

        self.lista = []
        for _ in range(5):
            self.n = instance(layout, QLineEdit("0"))
            self.lista.append(self.n)
        
        boton = instance(layout, QPushButton('Contar los mayores a 23'))
        boton.setDefault(True)
        boton.clicked.connect(self.contar)
        self.salida = instance(layout, QLabel("Resultado"))
        
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)


    def contar(self):
        c = 0
        for ctl in self.findChildren(QLineEdit):
            if int(ctl.text()) > 23: c += 1
        self.salida.setText(f"Resultado = {str(c)}")


if __name__ == '__main__':
    app = QApplication()
    css = '*{font-size: 20px; background-color: #688434; color: #000719;}'
    app.setStyleSheet(css)
    window = MainWindow()
    window.show()
    app.exec()
