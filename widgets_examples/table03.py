from PySide6.QtWidgets import (QApplication, 
                                QTableWidget,
                                QTableWidgetItem)


class Table(QTableWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.table = QTableWidget()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(data[0]))
        
        for x in range(len(self.data)):
            for y in range(len(self.data[x])):
                item = QTableWidgetItem(str(self.data[x][y]))
                self.table.setItem(x, y, item)
        self.table.show()


colors = [("Juan", 32, "1.87"),
          ["Ana", "77"],
          ("Luis", "41")
          ]


app = QApplication()
t = Table(colors)
app.exec()
