from PySide6.QtWidgets import QApplication, QMainWindow # reemplacé QWidget por QMainWindow

app = QApplication() # crea una instancia de la clase Aplicación 

window = QMainWindow() # crea una ventana propiamente dicha

window.show() # muestra la ventana

app.exec() # inicia el bucle de eventos
