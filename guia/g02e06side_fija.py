# Preguntar cuántas personas se van a cargar y luego solicitar sus edades,
# mostrando al final la edad promedio.

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(QMainWindow):
    def instance(self, lay, clase):
            v = clase
            lay.addWidget(v)
            return v

    def __init__(self):
        super().__init__()

        self.layout = layout = QVBoxLayout()
        self.t = self.instance(layout, QLabel('Cuántas personas se van a cargar?'))
        self.cantidad = self.instance(layout, QLineEdit())
        self.boton = boton = self.instance(layout, QPushButton('Carga'))
        boton.setDefault(True)
        boton.clicked.connect(self.carga)
        layout.addWidget(Caja("green"))
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def carga(self):
        self.quantity = int(self.cantidad.text())
        self.cantidad.setText("0")
        self.cantidad.close()
        self.t.setText("")
        self.boton.close()
        self.lista =[]
        print('carga')
        t = QLabel(f"Ingrese las edades de las {self.quantity} personas")
        self.layout.addWidget(t)
        for i in range(self.quantity):
            self.n = self.instance(self.layout, QLineEdit("0"))
            self.lista.append(self.n)
        promedio = QPushButton("Promediar")
        self.layout.addWidget(promedio)
        promedio.clicked.connect(self.promediar)

    def promediar(self):
        c = 0
        for ctl in self.findChildren(QLineEdit):
            c += int(ctl.text())
        self.t.setText(f"El promedio de edad es {str(c//self.quantity)}")

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.resize(500, 500)
    window.show()
    app.exec()
