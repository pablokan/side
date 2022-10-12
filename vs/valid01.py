from PySide6.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
from PySide6.QtGui import QIntValidator, QDoubleValidator, QFont
from PySide6.QtCore import Qt, QDate


class lineEditDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        e1 = QLineEdit()
        e1.setValidator(QIntValidator(10, 19))
        e1.setMaxLength(4)
        e1.setAlignment(Qt.AlignRight)
        e1.setFont(QFont("Arial", 20))

        e2 = QLineEdit()
        e2.setValidator(QDoubleValidator(0.99, 99.99, 2))
        e3 = QLineEdit()
        e3.setInputMask("+99_99_9999")

        e4 = QLineEdit()
        e4.textChanged.connect(self.textchanged)

        e5 = QLineEdit()
        e5.setEchoMode(QLineEdit.Password)

        e6 = QLineEdit("Hello PyQt5")
        e6.setReadOnly(True)
        e5.editingFinished.connect(self.enterPress)

        flo = QFormLayout()
        flo.addRow("integer validator", e1)
        flo.addRow("Double validator", e2)
        flo.addRow("Input Mask", e3)
        flo.addRow("Text changed", e4)
        flo.addRow("Password", e5)
        flo.addRow("Read Only", e6)

        self.setLayout(flo)
        self.setWindowTitle("QLineEdit Example")

    def textchanged(self, text):
        print("Changed: " + text)

    def enterPress(self):
        print("Enter pressed")


if __name__ == "__main__":
    app = QApplication()
    win = lineEditDemo()
    win.show()
    app.exec()
