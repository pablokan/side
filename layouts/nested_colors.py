from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget
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

        mainLayout = QHBoxLayout()
        layoutLeft = QVBoxLayout()
        layoutCenter = QVBoxLayout()
        layoutRight = QVBoxLayout()

        layoutLeft.addWidget(Color('red'))
        layoutLeft.addWidget(Color('yellow'))
        layoutLeft.addWidget(Color('purple'))
        mainLayout.addLayout(layoutLeft)

        layoutCenter.addWidget(Color('green'))
        mainLayout.addLayout(layoutCenter)

        layoutRight.addWidget(Color('red'))
        layoutRight.addWidget(Color('purple'))
        mainLayout.addLayout(layoutRight)

        mainLayout.setContentsMargins(0,0,0,0)
        mainLayout.setSpacing(20)

        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
