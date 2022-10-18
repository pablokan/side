from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QComboBox
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        def espacios(c):
            e = ''
            for _ in range(c):
                e += " "
            return e

        layout = QVBoxLayout()
        self.texto = QLabel()
        layout.addWidget(self.texto)
        combo = QComboBox()
        layout.addWidget(combo)
        lista = [
            "MacBook Air $249", 
            "Samsung Galaxy S22 Ultra $1200", 
            "USI Pen for Chromebook $29"
            ]
        newList = []
        for e in lista:
            posSigno = e.find("$")
            cE = 40 - len(e)
            newList.append(e[:posSigno] + espacios(cE) + e[posSigno:])

        combo.addItems(newList)
        combo.currentTextChanged.connect(self.text_changed)
        self.entrada = QLineEdit()
        layout.addWidget(self.entrada)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
       
    def text_changed(self, s):
        print(s)

if __name__ == '__main__':
    app = QApplication()
    css = '*{font-family: "Comic Mono"; font-size: 20px; background-color: black; color: yellow;}'
    app.setStyleSheet(css)
    window = MainWindow()
    window.show()
    app.exec()
