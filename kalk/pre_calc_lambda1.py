from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Works:
        self.button_1 = QPushButton('Button 1 manual', self)
        self.button_2 = QPushButton('Button 2 manual', self)
        layout.addWidget(self.button_1)
        layout.addWidget(self.button_2)

        self.button_1.clicked.connect(lambda x:self.button_pushed(1))
        self.button_2.clicked.connect(lambda x:self.button_pushed(2))

        # Doesn't work:
        self.buttons = []
        for idx in [3, 4]:
            button = QPushButton('Button {} auto'.format(idx), self)
            button.clicked.connect(lambda state=None, x=idx: self.button_pushed(x))
            self.buttons.append(button)
            layout.addWidget(button)


        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def button_pushed(self, num):
        print(f'Pushed button {num}')
        # print(self.sender()) None


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
