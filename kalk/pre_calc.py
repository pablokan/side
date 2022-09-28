from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setLayout(QVBoxLayout())
        self.checkbox_dict = dict()
        self.button_dict = dict()
        for i in range(0, 10):
            checkbox = QCheckBox(self, text='Checkbox' + str(i))
            self.layout().addWidget(checkbox)
            self.checkbox_dict[i] = checkbox
            button = QPushButton(self, text='PushButton' + str(i))
            self.layout().addWidget(button)
            self.button_dict[i] = button

        for i, button in enumerate(self.button_dict.values()):
            button.clicked.connect(lambda _, i=i: self.click_checkbox(i))

        self.show()

    def click_checkbox(self, i):
        self.checkbox = self.checkbox_dict[i]
        self.checkbox_state = self.checkbox.isChecked()
        self.checkbox.setChecked(not self.checkbox_state)



if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
