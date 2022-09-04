from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem

data = [("Juan", 32, "1.87"),
          ["Ana", "77"],
          ("Luis", "41")
          ]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        def instance(lay, clase):
            v = clase
            lay.addWidget(v)
            return v

        self.table = QTableWidget()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(data[0]))
        
        for x in range(len(data)):
            for y in range(len(data[x])):
                item = QTableWidgetItem(str(data[x][y]))
                self.table.setItem(x, y, item)

        layout = QVBoxLayout()
        self.t = instance(layout, QLabel('label'))
        self.n = instance(layout, QLineEdit())
        boton = instance(layout, QPushButton('label'))
        layout.addWidget(self.table)
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
