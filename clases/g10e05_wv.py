from PySide6.QtWidgets import (
    QApplication, QWidget, QMainWindow, 
    QLabel, QPushButton, QVBoxLayout, QLineEdit)

class Window(QWidget):
    def __init__(self, c):
        super().__init__()
        
        layout = QVBoxLayout()
        
        mensaje = QLabel("Carga")
        layout.addWidget(mensaje)

        for x in range(c):
            layout.addWidget(QLineEdit())

        b = QPushButton('Promedio')
        layout.addWidget(b)
        b.clicked.connect(self.promediar)

        self.salida = QLabel("Resultado")
        layout.addWidget(self.salida)

        self.setLayout(layout)

    def promediar(self):
        t = 0
        edades = self.findChildren(QLineEdit)
        for e in edades:
            t += int(e.text())
        self.salida.setText(f"Resultado = {t//len(edades)}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()

        mensaje = QLabel("Cuántas edades va a cargar?")
        layout.addWidget(mensaje)
        
        self.cantidad = QLineEdit() 
        layout.addWidget(self.cantidad)
        
        b = QPushButton('Carga')
        layout.addWidget(b)
        b.clicked.connect(self.cargar)
 
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def cargar(self):
        self.w = Window(int(self.cantidad.text()))
        self.w.show()

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
