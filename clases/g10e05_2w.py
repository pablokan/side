from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QPushButton, QVBoxLayout, QLineEdit)

class Window(QMainWindow):
    def __init__(self, c):
        super().__init__()
        layout = QVBoxLayout()
        for x in range(c):
            layout.addWidget(QLineEdit())
            
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.cantidad = QLineEdit() 
        layout.addWidget(self.cantidad)
        b = QPushButton('abre otra ventana y le pone lo que le mando')
        layout.addWidget(b)
        b.clicked.connect(self.abrirV)
 
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def abrirV(self):
        self.w = Window(int(self.cantidad.text()))
        self.w.show()

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
