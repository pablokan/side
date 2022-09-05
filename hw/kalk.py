from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        def instance(f, c, lay, clase):
            v = clase
            lay.addWidget(v, f, c)
            return v

        layout = QGridLayout()
        l = 0
        nList = []
        for x in range(3):
            for y in range(3):
                l += 1
                b = QPushButton(str(l))
                layout.addWidget(b, x, y)
                nList.append(b)

        for n in nList:
            print(n.text())
            n.clicked.connect(self.numero)
            ly = lambda: self.numero(n.text())
            n.clicked.connect(ly)



        resu = instance(x+1, 0, layout, QPushButton("Resultado"))
        self.t = instance(x+1, 1, layout, QLabel())
        resu.clicked.connect(self.resultado)
       
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)


    def numero(self, n):
        self.t.setText(str(n))

    def function_name(self):
        self.t.setText('xxxxxx')

    def resultado(self):
        for ctl in self.findChildren(QPushButton):        
            print(ctl.text())
    

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
