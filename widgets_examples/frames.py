from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QPushButton, QFrame
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 330)
        self.setStyleSheet("background-color: black;")

        self.frame1 = QFrame(self)
        self.frame1.setGeometry(10, 10, 480, 100)
        self.frame1.setStyleSheet("background-color: skyblue;")
        upperLayout = QVBoxLayout()
        for i in range(2):
            cT = QLineEdit()
            upperLayout.addWidget(cT)
        self.frame1.setLayout(upperLayout)

        self.frame2 = QFrame(self)
        self.frame2.setGeometry(10, 120, 480, 200)
        self.frame2.setStyleSheet("background-color: teal;")
        bottomLayout = QHBoxLayout()
        for i in range(2):
            cT = QLabel(f"Label {i}")
            cT.setStyleSheet("background-color: red")
            bottomLayout.addWidget(cT)
        self.frame2.setLayout(bottomLayout)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
