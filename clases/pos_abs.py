from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QPushButton, QFrame
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: black;")

        self.frame1 = QFrame(self)
        self.frame1.setGeometry(10, 10, 480, 100)
        self.frame1.setStyleSheet("background-color: red;")

        self.frame2 = QFrame(self)
        self.frame2.setGeometry(30, 100, 480, 200)
        self.frame2.setStyleSheet("background-color: green;")

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.setGeometry(0, 0, 500, 500)
    window.show()
    app.exec()
