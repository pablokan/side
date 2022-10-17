from PySide6.QtWidgets import (
    QApplication, QMainWindow)

from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(900, 700)

        def addMenuOption(m, cartel):
            op = QAction(cartel, self)
            op.triggered.connect(self.onMenuClick)
            m.addAction(op)

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")

        addMenuOption(file_menu, "&Open")
        addMenuOption(file_menu, "&Save")
        file_submenu = file_menu.addMenu("Preferences")
        addMenuOption(file_submenu, "&Keyboard Shortcuts")
        addMenuOption(file_submenu, "Kill Real &Madrid players")
        file_menu.addSeparator()
        addMenuOption(file_menu, "&Quit")
        
    def onMenuClick(self):
        op = self.sender().text()
        print(op)
        if op == "&Quit": 
            self.close()


def main():
    app = QApplication()
    css = '*{font-size: 40px; background-color: #f5432d; color: #230260;}'
    app.setStyleSheet(css)
    w = MainWindow()
    w.show()
    app.exec()

if __name__ == '__main__':
    main()
