from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        for x in range(5):
            layout.addWidget(QLabel(f"Texto {x}"))
        boton = QPushButton("Printear valores")
        layout.addWidget(boton)
        boton.clicked.connect(self.obtener)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def obtener(self):
        listaTextos = self.findChildren(QLabel)
        for t in listaTextos:
            print(t.text())


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
