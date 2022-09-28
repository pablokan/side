from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QButtonGroup, QRadioButton, QHBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        mainLayout = QVBoxLayout()

        w = QWidget()

        cs1 = QRadioButton("Fem", w)
        mainLayout.addWidget(cs1)
        cs2 = QRadioButton("Mas", w)
        mainLayout.addWidget(cs2)
        
        cs_group = QButtonGroup(w)
        cs_group.addButton(cs1)
        cs_group.addButton(cs2)

        ds1 = QRadioButton("Verde", w)
        mainLayout.addWidget(ds1)
        ds2 = QRadioButton("Azul", w)
        mainLayout.addWidget(ds2)

        ds_group = QButtonGroup(w)
        ds_group.addButton(ds1)
        ds_group.addButton(ds2)

        mainLayout.addWidget(w)

        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
