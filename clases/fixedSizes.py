from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QPushButton,
    QFrame
    )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 700) # tamaño fijo de la ventana (ancho y alto)
        self.setStyleSheet("background-color: red;") # color de fondo de la ventana

        frameAzul = QFrame(self)
        frameAzul.setGeometry(50, 200, 600, 400) # izquierda, arriba, ancho, alto
        frameAzul.setStyleSheet("background-color: blue;") # color de fondo del frame
        
        # y ahora los 3 botones seteados del mismo modo
        boton1 = QPushButton("5,5,100,20", frameAzul)
        boton1.setGeometry(5, 5, 100, 20)
        boton2 = QPushButton("30,30,200,40", frameAzul)
        boton2.setGeometry(30, 30, 200, 40)
        boton3 = QPushButton("100,100,400,80", frameAzul)
        boton3.setGeometry(100, 100, 400, 80)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()

