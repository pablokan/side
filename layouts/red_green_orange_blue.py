from turtle import color
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class Color(QLabel):
    def __init__(self, color, texto=''):
        super().__init__()
        self.setText(str(texto))
        self.setStyleSheet(f'background-color: {color}; color: white;')
        self.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.setFont(QFont("Victor Mono", 20))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        colorList = ['red', 'green', 'orange', 'blue']
        layout = QVBoxLayout()
        for i, c in enumerate(colorList):
            layout.addWidget(Color(c, i))

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.resize(300, 400)
    window.show()
    app.exec()
