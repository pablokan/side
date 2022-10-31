from dataclasses import dataclass

from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QLabel, 
    QLineEdit, 
    QPushButton, 
    )

from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


@dataclass
class Widget:
    string: str = ""
    fontF: str = "Arial"
    fontS: int = 15
    foreg: str = "black"
    backg: str = "white"
    hAlign: str ="hC"
    vAlign: str ="vC"
    border: int = 0
    radius: int = 15
    parent: any = None
    posAsize: tuple = (0, 0, 0, 0)

    def style(self, klass):
        align = {
            "aL": Qt.AlignLeft,
            "hC": Qt.AlignCenter,
            "aR": Qt.AlignRight,
            "aT": Qt.AlignTop, 
            "vC": Qt.AlignVCenter,
            "aB": Qt.AlignBottom
            }
        self.setText(str(self.string))
        self.setParent(self.parent)
        self.setGeometry(*self.posAsize)

        sts = fr"""
            {klass} {{
            background-color: {self.backg}; 
            color: {self.foreg};
            padding: 5; 
            border: {self.border}px solid;
            border-radius: {self.radius}px;
        }}
        """

        if isinstance(self, Input):
            self.selectAll()
        if isinstance(self, Button):
            stf =  fr"""
            {klass}:focus {{
                outline: none;
                font-weight: 900;
            }}
            """
            sts += stf
        else:
            self.setAlignment(align[self.hAlign] | align[self.vAlign])
            
        self.setFont(QFont(self.fontF, self.fontS))
        self.setStyleSheet(sts)
       

@dataclass
class Text(Widget, QLabel):
    def __post_init__(self):
        QLabel.__init__(self)
        self.style("Text")
        
@dataclass
class Input(Widget, QLineEdit):
    def __post_init__(self):
        QLineEdit.__init__(self)
        self.style("Input")

@dataclass
class Button(Widget, QPushButton):
    def __post_init__(self):
        QPushButton.__init__(self)
        self.style("Button")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 700) # tamaño fijo de la ventana (ancho y alto)
        self.setStyleSheet("background-color: red;") # color de fondo de la ventana

        # y ahora los 3 botones seteados del mismo modo

        boton1 = Button("5,5,120,40", parent=self, posAsize=(5,5,120,40))
        boton2 = Button("30,30,200,60", backg='cyan', parent=self, posAsize=(30,30,200,60))
        boton3 = Button("100,100,400,80", parent=self, posAsize=(100,100,400,80))

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()

