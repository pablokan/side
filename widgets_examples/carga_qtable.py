from PySide6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QLineEdit,
    QTableWidget,
    QPushButton
)
     
data = [("Juan", 32, "1.87"), ["Ana", "77"], ("Luis", "41")]

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD of gente")
        mainLayout = QVBoxLayout()
        nombre = self.nombre = QLineEdit("Nombre")
        mainLayout.addWidget(nombre)
        sueldo = self.sueldo = QLineEdit("Sueldo")
        mainLayout.addWidget(sueldo)
        boton = QPushButton("Cargar")
        mainLayout.addWidget(boton)
        boton.clicked.connect(self.carga)
        table = self.table = QTableWidget()
        mainLayout.addWidget(table)
        table.setRowCount(1)
        table.setColumnCount(2)
        self.iT = 0
        
        self.setLayout(mainLayout)

    def carga(self):
        item1 = QTableWidgetItem(self.nombre.text())
        item2 = QTableWidgetItem(self.sueldo.text())
        cF = self.table.rowCount()
        self.table.setItem(cF-1, 0, item1)
        self.table.setItem(cF-1, 1, item2)
        self.table.insertRow(cF)
        


if __name__ == "__main__":
    app = QApplication()
    window = Window()
    window.show()
    app.exec()
