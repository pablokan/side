from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import qdarktheme

app = QApplication()
win = QMainWindow()
push_button = QPushButton("PyQtDarkTheme!!")
win.setCentralWidget(push_button)

sts = qdarktheme.load_stylesheet()
f = open("darktheme.qss", "w")
f.write(sts)
f.close()
app.setStyleSheet(sts)
win.show()
app.exec()
