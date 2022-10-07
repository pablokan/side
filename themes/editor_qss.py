from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QWidget, QLabel,
    QLineEdit, QSpinBox, QPushButton, QPlainTextEdit, QVBoxLayout)
import sys


class EditorQSS(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.resize(480, 320)
        self.setWindowTitle("Editor QSS en vivo")

        self.editor = QPlainTextEdit()
        self.editor.setStyleSheet(
            "background-color: #212121; color: #e9e9e9; font-family: Consolas; font-size: 16px; ")
        self.editor.setFont("Consolas")
        self.editor.textChanged.connect(self.actualizar_estilos)

        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        self.setLayout(layout)

        self.show()

    def actualizar_estilos(self):
        qss = self.editor.toPlainText()
        try:
            self.parent.setStyleSheet(qss)
        except:
            pass