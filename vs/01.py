from PySide6.QtWidgets import QApplication, QWidget

app = QApplication() # crea una instancia de la clase Aplicación 
window = QWidget() # crea una ventana como widget 
# (todos los objetos que veremos son widgets, los botones por ejemplo)
window.show() # muestra la ventana
app.exec() # inicia el bucle de eventos

