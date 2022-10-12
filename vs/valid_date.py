from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QDateEdit
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QDate

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        date = QDateEdit(self) 
        layout.addWidget(date)
        d = QDate(2020, 6, 10) 
        date.setDate(d) 
        value = date.date() 
        print(value)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def function_name(self):
        self.texto.setText(f'Hola {self.entrada.text()}')

if __name__ == '__main__':
    app = QApplication()
    css = '*{font-size: 30px; background-color: darkblue; color: skyblue;}'
    app.setStyleSheet(css)
    window = MainWindow()
    window.show()
    app.exec()
