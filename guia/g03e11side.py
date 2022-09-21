# (g03e11) Cargar en listas los nombres y fechas de nacimiento de varias personas, 
# luego recorrerlo y mostrar los nombres de los mayores de edad.
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QFormLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])

        # In QListWidget there are two separate signals for the item, and the str
        widget.currentItemChanged.connect( self.index_changed )
        widget.currentTextChanged.connect( self.text_changed )

        self.setCentralWidget(widget)


    def index_changed(self, i): # Not an index, i is a QListItem
        print(i.text())

    def text_changed(self, s): # s is a str
        print(s)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()

