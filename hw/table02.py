from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, 
                                QMainWindow,
                                QTableWidget,
                                QTableWidgetItem)

colors = [("Red", "#FF0000"),
          ("Green", "#00FF00"),
          ("Blue", "#0000FF"),
          ("Black", "#000000"),
          ("White", "#FFFFFF"),
          ("Electric Green", "#41CD52"),
          ("Dark Blue", "#222840"),
          ("Yellow", "#F9E56d")]


app = QApplication()

table = QTableWidget()
table.setRowCount(len(colors))
table.setColumnCount(len(colors[0]))
table.setHorizontalHeaderLabels(["Name", "Hex Code"])


for x in range(len(colors)):
    for y in range(len(colors[x])):
        item = QTableWidgetItem(colors[x][y])
        table.setItem(x, y, item)


   
table.show()
app.exec()
