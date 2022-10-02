from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class Window(QMainWindow):
    def __init__(self, mensaje):
        super().__init__()
        self.setCentralWidget(QLabel(mensaje))
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        b = QPushButton('abre otra ventana y le pone lo que le mando')
        b.clicked.connect(self.abrirV)
        self.setCentralWidget(b)


    def abrirV(self):
        self.w = Window("cualquier argumento")
        self.w.show()

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
