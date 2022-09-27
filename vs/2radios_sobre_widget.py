from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QButtonGroup, QRadioButton, QHBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        mainLayout = QVBoxLayout()

        cs1 = QRadioButton("Fem", self)
        mainLayout.addWidget(cs1)
        cs2 = QRadioButton("Mas", self)
        mainLayout.addWidget(cs2)
        
        cs_group = QButtonGroup(self)
        cs_group.addButton(cs1)
        cs_group.addButton(cs2)

        ds1 = QRadioButton("Verde", self)
        mainLayout.addWidget(ds1)
        ds2 = QRadioButton("Azul", self)
        mainLayout.addWidget(ds2)

        ds_group = QButtonGroup(self)
        ds_group.addButton(ds1)
        ds_group.addButton(ds2)

        self.setLayout(mainLayout)


if __name__ == '__main__':
    app = QApplication()
    widget = MainWindow()
    widget.show()
    app.exec()
