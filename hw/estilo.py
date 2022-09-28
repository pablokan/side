from turtle import color
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class Style():
    def __init__(self, text="", fontF="Arial", fontS=15, fore="black", 
                back="white", horizontalAlign="hC", verticalAlign="vC"):
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


class Input(QLineEdit, Style):
    def __init__(self, text="", fontF="Arial", fontS=15, fore="black", 
                back="white", horizontalAlign="hC", verticalAlign="vC"):
        QLineEdit.__init__(self)
        Style.__init__(self, text, fontF, fontS, fore, 
                back, horizontalAlign, verticalAlign)
        
           

class Text(QLabel, Style):
    """
    alignment = {
            "aL": Qt.AlignLeft,
            "hC": Qt.AlignCenter,
            "aR": Qt.AlignRight,
            "aT": Qt.AlignTop, 
            "vC": Qt.AlignVCenter,
            "aB": Qt.AlignBottom
            }
    """
    def __init__(self, text="", fontF="Arial", fontS=15, fore="black", 
                back="white", horizontalAlign="hC", verticalAlign="vC"):
        QLabel.__init__(self)
        Style.__init__(self, text, fontF, fontS, fore, 
                back, horizontalAlign, verticalAlign)
        
        


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        colorList = ['red', 'green', 'orange', 'blue']
        alineado = [
            ("hC", "vC"), 
            ("aL", "aB"),
            ("aR", "aT"),
            ("hC", "vC")
            ]
        layout = QVBoxLayout()
        for c, a in zip(colorList, alineado):
            t = f"texto #{c}"
            layout.addWidget(Text(t, "NovaMono", 20, "cyan", c, a[0], a[1]))

        layout.addWidget(Text("pablo", "Victor Mono", 10, "sky blue", "blue", "aR", "aT"))
        layout.addWidget(Text("kan", "Victor Mono", 30, "red", "orange", "aL", "aB"))
        layout.addWidget(Text("Manchester City"))
        layout.addWidget(Input(fore="red", back="yellow"))
        layout.addWidget(Text("Liverpool", horizontalAlign="aR"))
        layout.addWidget(Text("lo mismo"))
        layout.addWidget(Input("lo mismo"))

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.resize(300, 400)
    window.show()
    app.exec()
