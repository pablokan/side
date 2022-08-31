# Preguntar cuántas personas se van a cargar y luego solicitar sus edades,
# mostrando al final la edad promedio.

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        def instance(lay, clase):
            v = clase
            lay.addWidget(v)
            return v

        self.w = AnotherWindow()
        layout = QVBoxLayout()
        self.t = instance(layout, QLabel('Cuántas personas se van a cargar?'))
        self.n = instance(layout, QLineEdit())
        boton = instance(layout, QPushButton('Carga'))
        boton.setDefault(True)
        boton.clicked.connect(self.carga)
        
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def carga(self):
        print('carga')
        xMain = self.pos().x()
        yMain = self.pos().y()
        xSec = xMain + 200
        ySec = yMain + 100
        self.w.move(xSec, ySec)
        for self.x in range(5):
            n = QLineEdit("0")
            self.w.layout.addWidget(n)
            self.lista.append(n)
        self.w.show()


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
