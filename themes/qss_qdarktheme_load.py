from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import qdarktheme

app = QApplication()
win = QMainWindow()
push_button = QPushButton("PyQtDarkTheme!!")
win.setCentralWidget(push_button)

app.setStyleSheet(qdarktheme.load_stylesheet())
win.show()
app.exec()
