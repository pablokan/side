# importing libraries 

from PySide6.QtWidgets import * 

from PySide6 import QtCore, QtGui 

from PySide6.QtGui import * 

from PySide6.QtCore import * 

import sys 

  
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("Python ")
  
        # setting geometry
        self.setGeometry(100, 100, 600, 400)
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()
  
    # method for widgets
    def UiComponents(self):
  
        # creating a combo box widget
        self.combo_box = QComboBox(self)
  
        # setting geometry of combo box
        self.combo_box.setGeometry(200, 150, 150, 30)
  
        # making combo box editable
        self.combo_box.setEditable(True)
  
        # geek list
        geek_list = ["Sayian", "Super Sayian", "Super Sayian 2", "Super Sayian B"]
  
        # adding list of items to combo box
        self.combo_box.addItems(geek_list)
  
        # adding background color to the view part of combo box
        self.combo_box.setStyleSheet("QListView"
                                     "{"
                                     "background-color: lightgreen;"
                                     "}")
  
  
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())
