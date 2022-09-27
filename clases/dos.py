from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QLabel, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout() # esquema 
        for x in range(5):
            texto = QLabel(f'Texto #{x+1}') # instancio texto estático
            layout.addWidget(texto) # agrego el texto al esquema

        entrada = QLineEdit() # instancio un caja de texto
        layout.addWidget(entrada) # agrego la caja de texto al esquema

        # estas 3 líneas de ahora en más son automáticas
        centralWidget = QWidget() # creo un widget que servirá de base del esquema
        centralWidget.setLayout(layout) # le paso el esquema 
        self.setCentralWidget(centralWidget) # lo centro

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
