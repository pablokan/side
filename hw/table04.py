from PySide6.QtWidgets import *
					

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.title = 'PyQt5 - QTableWidget'

		self.createTable()

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.tableWidget)
		self.setLayout(self.layout)

		#Show window
		self.show()

	#Create table
	def createTable(self):
		self.tableWidget = QTableWidget()

		#Row count
		self.tableWidget.setRowCount(4)

		#Column count
		self.tableWidget.setColumnCount(2)

		self.tableWidget.setItem(0,0, QTableWidgetItem("Name"))
		self.tableWidget.setItem(0,1, QTableWidgetItem("City"))
		self.tableWidget.setItem(1,0, QTableWidgetItem("Aloysius"))
		self.tableWidget.setItem(1,1, QTableWidgetItem("Indore"))
		self.tableWidget.setItem(2,0, QTableWidgetItem("Alan"))
		self.tableWidget.setItem(2,1, QTableWidgetItem("Bhopalititititititititititititit"))
		self.tableWidget.setItem(3,0, QTableWidgetItem("Arnavi"))
		self.tableWidget.setItem(3,1, QTableWidgetItem("Mandsaur"))

		#Table will fit the screen horizontally
		self.tableWidget.horizontalHeader().setStretchLastSection(True)
		self.tableWidget.horizontalHeader().setSectionResizeMode(
			QHeaderView.Stretch)

if __name__ == '__main__':
	app = QApplication()
	ex = App()
	app.exec()
