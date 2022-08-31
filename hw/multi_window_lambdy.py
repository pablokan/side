from random import randint

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window1 = AnotherWindow()
        self.window1.hide()
        l = QVBoxLayout()
        button1 = QPushButton("Push for Window")
        l.addWidget(button1)
        button1.clicked.connect(lambda : self.window1.show()) 

        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)


app = QApplication()
w = MainWindow()
w.show()
app.exec()
