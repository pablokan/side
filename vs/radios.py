from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QPushButton, QRadioButton, QButtonGroup
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        def instance(lay, clase):
            v = clase
            lay.addWidget(v)
            return v

        hbox1 = QHBoxLayout()
        rb1 = QRadioButton("Femenino", self)
        rb1.toggled.connect(self.updateLabel1)
        rb2 = QRadioButton("Masculino", self)
        rb2.toggled.connect(self.updateLabel1)
        hbox1.addWidget(rb1)
        hbox1.addWidget(rb2)
        gb1 = QButtonGroup()
        gb1.addButton(rb1)
        gb1.addButton(rb2)

        hbox2 = QHBoxLayout()
        rb3 = QRadioButton("Verde")
        rb3.toggled.connect(self.updateLabel2)
        rb4 = QRadioButton("Celeste")
        rb4.toggled.connect(self.updateLabel2)
        hbox2.addWidget(rb3)
        hbox2.addWidget(rb4)
        gb2 = QButtonGroup()
        gb2.addButton(rb3)
        gb2.addButton(rb4)


        mainLayout = QVBoxLayout()
        mainLayout.addLayout(hbox1)
        mainLayout.addLayout(hbox2)
        self.t = instance(mainLayout, QLabel('label'))
        self.n = instance(mainLayout, QLineEdit())
        
        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

    def updateLabel1(self):
        rbtn = self.sender()
        if rbtn.isChecked() == True:
            self.t.setText(rbtn.text())

    def updateLabel2(self):
        rbtn = self.sender()
        if rbtn.isChecked() == True:
            self.t.setText(rbtn.text())

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
