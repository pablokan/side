#1: Almacenar en dos listas paralelas, nombres y sexos de 8 personas. 
#2: Recorrerlas y mostrar los nombres de las mujeres. 

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QRadioButton)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        def instance(lay, clase):
            v = clase
            lay.addWidget(v)
            return v

        layout = QVBoxLayout()
        self.t = instance(layout, QLabel('label'))
        self.n = instance(layout, QLineEdit())
        boton = instance(layout, QPushButton('label'))
        boton.clicked.connect(self.function_name)
        
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def function_name(self):
        self.t.setText('xxxxxx')

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
