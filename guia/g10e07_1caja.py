# Ingresar la lluvia caída en milímetros para cada día de la semana. 
# Mostrar al final el total de lluvia caída y el nombre del día que más llovió.

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QFormLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.l = []
        self.t = 0
        mainLayout = QVBoxLayout()
        self.c = 0
        self.dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        self.titulo = titulo = QLabel(f"lluvia caída el día lunes")
        mainLayout.addWidget(titulo)
        self.lluviaDiaria = QLineEdit()
        mainLayout.addWidget(self.lluviaDiaria)
        self.boton = boton = QPushButton('Carga de lluvia semanal')
        mainLayout.addWidget(boton)
        boton.setDefault(True)
        boton.clicked.connect(self.contar)
        self.salida = QLabel("Resultado")
        mainLayout.addWidget(self.salida)
        
        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)


    def contar(self):
        self.c += 1
        lluviaDiaria = int(self.lluviaDiaria.text())
        self.t += lluviaDiaria
        dia = self.dias.pop(0)
        self.l.append((lluviaDiaria, dia))
        print(self.l)
        self.lluviaDiaria.setFocus()
        
        if self.c < 7:
            self.titulo.setText(f"lluvia caída el dia {self.dias[0]}")
        else:
            self.titulo.deleteLater()
            self.lluviaDiaria.deleteLater()
            self.boton.deleteLater()
            m = max(self.l)[1]
            self.salida.setText(f"Total: {self.t}-Día mas lluvioso: {m}")


if __name__ == '__main__':
    app = QApplication()
    css = '*{font-size: 20px; background-color: #c1dddf; color: #5f00ec;}'
    app.setStyleSheet(css)
    window = MainWindow()
    window.show()
    app.exec()

