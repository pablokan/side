from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        def instance(lay, clase):
            v = clase
            lay.addWidget(v)
            return v

        layout = QVBoxLayout()
        self.t = instance(layout, QLabel('label'))
        self.n = instance(layout, QLineEdit())
        boton1 = instance(layout, QPushButton('b1'))
        boton1.clicked.connect(lambda: self.f1("Juan", 32))
        boton1.clicked.connect(self.f2)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def f1(self, n, e):
        self.t.setText('xxxxxx')
        print(n, e)

    def f2(self):
        print(self.sender().text())

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
