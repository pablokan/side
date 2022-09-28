from curses.ascii import BS
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        mainLayout = QVBoxLayout()
        self.t = QLineEdit()
        mainLayout.addWidget(self.t)
        self.r = QLineEdit()
        mainLayout.addWidget(self.r)
        grilla = QGridLayout()
        mainLayout.addLayout(grilla)
        i = 0
        
        for x in range(3):
            for y in range(3):
                i += 1
                b = QPushButton(str(i))
                b.clicked.connect(lambda state=None, x=i: self.numero(x))
                grilla.addWidget(b, x, y)
        
        colu = 0
        for cero in ['0', '00', '000']:
            b = QPushButton(str(cero))
            b.clicked.connect(lambda state=None, x=cero: self.numero(x))
            grilla.addWidget(b, x+1, colu)
            colu += 1
        
        signosLay = QHBoxLayout()
        for signo in ['+', '-', '*', '/']:
            b = QPushButton(signo)
            signosLay.addWidget(b)
            b.clicked.connect(lambda state=None, x=signo: self.numero(x))

        mainLayout.addLayout(signosLay)
        resu = QPushButton("=")
        mainLayout.addWidget(resu)
        resu.clicked.connect(self.resultado)
       
        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

    def numero(self, n):
        qq = self.t.text() + str(n)
        self.t.setText(qq)

    def resultado(self):
        self.r.setText(str(eval(self.t.text())))


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()

"""
False5
5False ----> cuando clickeo el 7, pone el número anterior: 5 + False ...
False7 ----> ... y False más el 7 clickeado
"""
