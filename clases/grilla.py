import os, sys
sys.path.append(os.path.abspath('libs'))

from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout, QGridLayout)
from styles import Text, Input, Button

class Caja(Text):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f'background-color: {color};')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        for i in range(5):
            layout.addWidget(Caja("red"), i, i)
        layout.addWidget(Caja("green"), 0, 2)
        layout.addWidget(Caja("blue"), 1, 5)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
