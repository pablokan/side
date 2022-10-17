# 1: Almacenar en dos listas paralelas, nombres y sexos de 8 personas.
# 2: Recorrerlas y mostrar los nombres de las mujeres.

from tkinter import mainloop
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QGridLayout,
    QButtonGroup,
    QMessageBox,
)


class Grilla(QWidget):
    def __init__(self):
        super().__init__()

        cuadricula = QGridLayout()

        for x in range(8):
            cuadricula.addWidget(QLineEdit(f"nombre{x}"), x, 0)
            bg = QButtonGroup(self)
            rbF = QRadioButton("Femenino", self)
            rbF.setChecked(True)
            rbM = QRadioButton("Masculino", self)
            cuadricula.addWidget(rbF, x, 1)
            cuadricula.addWidget(rbM, x, 2)
            bg.addButton(rbF)
            bg.addButton(rbM)

        self.setLayout(cuadricula)

    def updateLabel(self):
        for ctl in self.findChildren(QRadioButton):
            print(ctl.text())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mainLayout = QVBoxLayout()
        grilla = Grilla()
        mainLayout.addWidget(grilla)

        b = QPushButton("Mostrar nombres de mujeres")
        mainLayout.addWidget(b)
        b.clicked.connect(self.procesar)
        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

    def procesar(self):
        nombres = self.findChildren(QLineEdit)
        sexos = self.findChildren(QButtonGroup)
        chicas = ""
        for nombre, sexo in zip(nombres, sexos):
            if sexo.checkedId() == -2:
                print(nombre.text())
                chicas += nombre.text() + "\n"

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Mujeres")
        dlg.setText(chicas)
        dlg.exec()


if __name__ == "__main__":
    app = QApplication()
    css = '*{font-size: 20px; background-color: #c6f5c7; color: #850a30;}'
    app.setStyleSheet(css)
    window = MainWindow()
    window.show()
    app.exec()
