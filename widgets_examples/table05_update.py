import os, sys
sys.path.append(os.path.abspath('libs'))

from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem)
from styles import Text, Input, Button

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)

        self.tableWidget.setItem(0,0, QTableWidgetItem("Name"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("City"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Aloysius"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Indore"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Alan"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Bhopalititititititititititititit"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Arnavi"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Mandsaur"))
        layout.addWidget(self.tableWidget)
        self.entrada = Input('Input', fontF='Calibri', fontS=20)
        layout.addWidget(self.entrada)
        self.texto = Text('Text', foreg='cyan', backg='#123456', hAlign='aL', border=3, radius=0)
        layout.addWidget(self.texto)
        boton = Button('Button', foreg='red', backg='yellow')
        layout.addWidget(boton)
        boton.setDefault(True)
        boton.clicked.connect(self.functionName)
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def functionName(self):
        selRow = self.tableWidget.selectedItems()
        print(f'Debugging ######## {selRow[0].row()=} #########')
        r = int(selRow[0].row())
        self.tableWidget.setItem(r,0, QTableWidgetItem("Pol"))
        self.tableWidget.setItem(r,1, QTableWidgetItem("Kan"))

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
