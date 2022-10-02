from dataclasses import dataclass

from PySide6.QtWidgets import (
    QApplication, 
    QWidget, 
    QMainWindow, 
    QVBoxLayout,
    QLabel, 
    QLineEdit, 
    QPushButton
    )

from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


@dataclass
class Widget:
    string: str = ""
    fontF: str = "Arial"
    fontS: int = 15
    foreg: str = "black"
    backg:str = None
    hAlign: str ="hC"
    vAlign: str ="vC"
    border: str = "0"
    radius: str = "15"
    moreStyle: str =""    

    def style(self):
        align = {
            "aL": Qt.AlignLeft,
            "hC": Qt.AlignCenter,
            "aR": Qt.AlignRight,
            "aT": Qt.AlignTop, 
            "vC": Qt.AlignVCenter,
            "aB": Qt.AlignBottom
            }
        self.setText(str(self.string))
        style = f"""
            background-color: {self.backg}; 
            color: {self.foreg};
            padding: 5; 
            border: {self.border}px solid;
            border-radius: {self.radius}px;
        """
        self.setStyleSheet(style + self.moreStyle)
        if isinstance(self, QLineEdit):
            self.selectAll()
        if not isinstance(self, QPushButton):
            self.setAlignment(align[self.hAlign] | align[self.vAlign])
        self.setFont(QFont(self.fontF, self.fontS))


@dataclass
class Text(Widget, QLabel):
    def __post_init__(self):
        QLabel.__init__(self)
        self.style()
        
@dataclass
class Input(Widget, QLineEdit):
    def __post_init__(self):
        QLineEdit.__init__(self)
        self.style()

@dataclass
class Button(Widget, QPushButton):
    def __post_init__(self):
        QPushButton.__init__(self)
        self.style()

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

        b = Button("Botón", "Victor Mono", 30, "red", "orange", radius=40, moreStyle='height: 200px')
        layout.addWidget(Text("pablo", "Victor Mono", 20, "grey", "blue", "aR", "aT"))
        layout.addWidget(Text("kan", "Victor Mono", 20, "red", "orange", "aL", "aB", "border: 3px solid"))
        layout.addWidget(b)
        layout.addWidget(Text("Manchester City"))
        layout.addWidget(Input(foreg="red", backg="yellow"))
        layout.addWidget(Text("Liverpool", hAlign="aR"))
        layout.addWidget(Text("lo mismo", border=10))
        layout.addWidget(Input("lo mismo"))
        
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.resize(500, 800)
    window.show()
    app.exec()

