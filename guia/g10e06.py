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
        self.texto = QLabel('Promedio')
        layout.addWidget(self.texto)
        self.entrada = QLineEdit()
        layout.addWidget(self.entrada)
        boton = QPushButton('Promedio')
        layout.addWidget(boton)
        boton.clicked.connect(self.promedio)
        self.listaMayores = listaMayores = QListWidget()
        layout.addWidget(self.listaMayores)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def uno(self, item):
        print("item:", item.text())

    def dos(self, stringy):
        print("string:", stringy)    

    def promedio(self):
        t = 0
        lenny = self.lista.count()
        lN = []
        for i in range(lenny):
            n = int(self.lista.item(i).text())
            lN.append(n)
            t += n
        prom = t//lenny
        self.texto.setText(str(prom))

        for n in lN:
            if n >= prom:
                self.listaMayores.addItem(str(n))

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
