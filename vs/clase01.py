from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QListWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.lista = lista = QListWidget()
        self.lista.addItems(["11", "22", "12", "15"])
        lista.currentItemChanged.connect(self.uno)
        lista.currentTextChanged.connect(self.dos)
        layout.addWidget(self.lista)
        self.texto = QLabel('label')
        layout.addWidget(self.texto)
        self.entrada = QLineEdit()
        layout.addWidget(self.entrada)
        boton = QPushButton('Promedio')
        layout.addWidget(boton)
        boton.clicked.connect(self.promedio)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def uno(self, item):
        print("item:", item.text())

    def dos(self, stringy):
        print("string:", stringy)    

    def promedio(self):
        for i in range(self.lista.count()):
            print(self.lista.item(i).text())

        #@self.texto.setText(f'Hola {self.entrada.text()}')

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
