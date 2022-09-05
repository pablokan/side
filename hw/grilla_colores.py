from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QLineEdit, QPushButton
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
        def instance(lay, clase):
            v = clase
            lay.addWidget(v)
            return v

        mainLayout = QGridLayout()

        colorFila = ['red', 'green', 'orange', 'blue']
        for x in range(4):
            for y in range(4):
                mainLayout.addWidget(Color(f'{colorFila[x]}', f'{x},{y}'), x, y)

        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.resize(700, 500)
    window.show()
    app.exec()
