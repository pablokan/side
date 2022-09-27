# Ingresar la lluvia caída en milímetros para cada día de la semana. 
# Mostrar al final el total de lluvia caída y el nombre del día que más llovió.

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QFormLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mainLayout = QVBoxLayout()
        titulo = QLabel("lluvia caída x día de semana")
        mainLayout.addWidget(titulo)
        layout = QFormLayout()
        self.dias = dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        for dia in dias: 
            layout.addRow(dia, QLineEdit())
        mainLayout.addLayout(layout)
        boton = QPushButton('Lluvia')
        mainLayout.addWidget(boton)
        boton.setDefault(True)
        boton.clicked.connect(self.contar)
        self.salida = QLabel("Resultado")
        mainLayout.addWidget(self.salida)
        
        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)


    def contar(self):
        l = []
        t = 0
        for cll, dia in zip(self.findChildren(QLineEdit), self.dias):
            lluviaDiaria = int(cll.text())
            t += lluviaDiaria
            l.append((lluviaDiaria, dia))
        print(l)
        m = max(l)[1]
        self.salida.setText(f"{t}-{m}")


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()

