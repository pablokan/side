from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.acum = QLineEdit()
        layout.addWidget(self.acum)
        self.buttons = []
        for i in range(1, 5):
            button = QPushButton('Button {} auto'.format(i), self)
            button.clicked.connect(lambda state=None, x=i: self.button_pushed(x))
            self.buttons.append(button)
            layout.addWidget(button)


        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def button_pushed(self, num):
        print(f'Pushed button {num}')
        qq = self.acum.text() + str(num)
        self.acum.setText(qq)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
