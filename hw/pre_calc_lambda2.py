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
        boton = instance(layout, QPushButton('label'))
        boton.clicked.connect(self.connections)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)


    # self.widgets is a dictionary with keys for the group of buttons, 
    # to make it short let's say it have 2 buttons[QToolButton], linked to their keys: 'play' and 'stop'.
    def connections(self):
        for group in self.widgets:
            self.widgets[group].clicked.connect(lambda g=group: self.openMenu(g))

    def openMenu(self,group):
        print(group)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
