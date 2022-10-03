from PySide6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QLineEdit,
    QPushButton
)

        

data = [("Juan", 32, "1.87"),
          ["Ana", "77"],
          ("Luis", "41")
          ]


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD of gente")
        outerLayout = QVBoxLayout()
        gridLayout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(data[0]))
        
        for x in range(len(data)):
            for y in range(len(data[x])):
                item = QTableWidgetItem(str(data[x][y]))
                self.table.setItem(x, y, item)

        self.search = QLineEdit()
        gridLayout.addWidget(self.search)
        self.search.textChanged.connect(self.update_filter)

        gridLayout.addWidget(self.table)
        outerLayout.addLayout(gridLayout)
        self.setLayout(outerLayout)

    def update_filter(self):
        name = self.search.text().lower()
        for row in range(self.table.rowCount()):
            item = self.table.item(row, 0)
            self.table.setRowHidden(row, name not in item.text().lower())

if __name__ == "__main__":
    app = QApplication()
    window = Window()
    window.show()
    app.exec()
