from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

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
        self.tableWidget.setItem(2,1, QTableWidgetItem("Bhopa"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Arnavi"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Mandsaur"))
        layout.addWidget(self.tableWidget)
        self.entrada = QLineEdit('Input')
        layout.addWidget(self.entrada)
        self.texto = QLabel('Text')
        layout.addWidget(self.texto)
        boton = QPushButton('Button')
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
    app.setStyleSheet('*{font-size: 30px; background-color:midnightblue; color:"sky blue";}')
    window = MainWindow()
    window.show()
    app.exec()
