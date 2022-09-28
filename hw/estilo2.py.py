# ta fallido por ahora, capaz no tiene arreglo igual
# estilo.py funciona bien pero duplica código

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class Style():
    def __init__(self, Class, text="", fontF="Arial", fontS=15, fore="black", 
                back="white", horizontalAlign="hC", verticalAlign="vC"):
        Class.__init__(Class(), text="", fontF="Arial", fontS=15, fore="black", 
                back="white", horizontalAlign="hC", verticalAlign="vC")
        align = {
            "aL": Qt.AlignLeft,
            "hC": Qt.AlignCenter,
            "aR": Qt.AlignRight,
            "aT": Qt.AlignTop, 
            "vC": Qt.AlignVCenter,
            "aB": Qt.AlignBottom
            }
        self.setText(str(text))
        self.setStyleSheet(f'background-color: {back}; color: {fore};')
        self.setAlignment(align[horizontalAlign] | align[verticalAlign])
        self.setFont(QFont(fontF, fontS))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # layout.addWidget(Style(QLabel, "pablo", "Victor Mono", 10, "sky blue", "blue", "aR", "aT"))
        #layout.addWidget(Style(QLabel, "kan", "Victor Mono", 30, "red", "orange", "aL", "aB"))
        # layout.addWidget(Style(QLabel, "Manchester City"))
        #layout.addWidget(Style(QLineEdit, fore="red", back="yellow"))
        layout.addWidget(Style(QLabel, "Liverpool", horizontalAlign="aR"))
        # layout.addWidget(Style(QLabel, "lo mismo"))
        # layout.addWidget(Style(QLineEdit, "lo mismo"))

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.resize(300, 400)
    window.show()
    app.exec()
