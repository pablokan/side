from turtle import color
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class Style():
    def __init__(self, text="", fontF="Arial", fontS=15, fore="black", 
                back="white", horizontalAlign="hC", verticalAlign="vC",
                moreStyle=""):
        align = {
            "aL": Qt.AlignLeft,
            "hC": Qt.AlignCenter,
            "aR": Qt.AlignRight,
            "aT": Qt.AlignTop, 
            "vC": Qt.AlignVCenter,
            "aB": Qt.AlignBottom
            }
        self.setText(str(text))
        style = f"""
            background-color: {back}; 
            color: {fore};
            padding: 5; 
            
        """
        self.setStyleSheet(style + moreStyle)
        if not isinstance(self, QPushButton):
            self.setAlignment(align[horizontalAlign] | align[verticalAlign])
        self.setFont(QFont(fontF, fontS))

class Button(QPushButton, Style):
    def __init__(self, text="", fontF="Arial", fontS=15, fore="black", 
                back="white", moreStyle=""):
        QPushButton.__init__(self)
        Style.__init__(self, text, fontF, fontS, fore, 
                back, moreStyle)
    
class Input(QLineEdit, Style):
    def __init__(self, text="", fontF="Arial", fontS=15, fore="black", 
                back="white", horizontalAlign="hC", verticalAlign="vC", moreStyle=""):
        QLineEdit.__init__(self)
        Style.__init__(self, text, fontF, fontS, fore, 
                back, horizontalAlign, verticalAlign, moreStyle)
        
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
                back="white", horizontalAlign="hC", verticalAlign="vC", moreStyle=""):
        QLabel.__init__(self)
        Style.__init__(self, text, fontF, fontS, fore, 
                back, horizontalAlign, verticalAlign, moreStyle)
        
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

        b = Button("Botón", "Victor Mono", 30, "red", "orange")
        layout.addWidget(Text("pablo", "Victor Mono", 10, "sky blue", "blue", "aR", "aT"))
        layout.addWidget(Text("kan", "Victor Mono", 30, "red", "orange", "aL", "aB", "border: 3px solid"))
        layout.addWidget(b)
        layout.addWidget(Text("Manchester City"))
        layout.addWidget(Input(fore="red", back="yellow"))
        layout.addWidget(Text("Liverpool", horizontalAlign="aR"))
        layout.addWidget(Text("lo mismo", moreStyle='border: 5px solid;'))
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

