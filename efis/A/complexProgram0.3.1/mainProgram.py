from libraries.complexLibs import *

class WindowEditar(QWidget):
    def __init__(self, filaSeleccionada, tabla, claves, datos):
        super().__init__()
        self.tabla = tabla
        self.claves = claves
        self.layout = layout = QVBoxLayout()

        fila = filaSeleccionada[0].row()
        self.id = tabla.item(fila,0).text()
        self.listaDatos = []
        vueltita = 0
        for dato in datos:
            if dato != "ID: ":
                vueltita += 1
                fila = filaSeleccionada[vueltita].row()
                fId = tabla.item(fila,vueltita).text()
                dato = QLabel(dato)
                tituloTabla(dato, layout, 20, 20)
                self.entrada = QLineEdit(fId)
                casillaTabla(self.entrada, layout, 20, 50)
                self.listaDatos.append(self.entrada)

        self.botonGuardar = QPushButton("Guardar")
        botonMainMenu(self.botonGuardar, layout, self.guardadoDatos)

        self.setLayout(layout)

    def guardadoDatos(self):
        string = ""
        if self.botonGuardar.clicked:
            for carga in self.listaDatos:
                dato = carga.text()
                string = string + "'" + dato +"',"
        string = string[:-1]
        actualizar(string, self.claves, self.tabla, self.id)

class WindowCarga(QWidget):
    def __init__(self, datos, claves, tabla):
        super().__init__()
        self.tabla = tabla
        self.claves = claves[4:]
        self.layout = layout = QVBoxLayout()

        self.listaDatos = []
        for dato in datos:
            if dato != "ID: ":
                dato = QLabel(dato)
                tituloTabla(dato, layout, 20, 20)
                self.entrada = QLineEdit()
                casillaTabla(self.entrada, layout, 20, 50)
                self.listaDatos.append(self.entrada)

        self.botonGuardar = QPushButton("Guardar")
        botonMainMenu(self.botonGuardar, layout, self.guardadoDatos)

        self.setLayout(layout)

    def guardadoDatos(self):
        string = ""
        if self.botonGuardar.clicked:
            for carga in self.listaDatos:
                dato = carga.text()
                string = string + "'" + dato +"',"
        string = string[:-1]
        guardado(string, self.claves, self.tabla)

class WindowReservas(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = layout = QVBoxLayout()

        botonTabla(self, "Nuevo", 20, 20, self.nuevaReserva)
        botonTabla(self, "Borrar", 180, 20, self.borrarReserva)

        columnas = ("ID: ","Cliente: ", "Salon: ", "Fecha: ")
        self.datos = columnas
        base = "reservas"
        self.tabla = base
        claveColumnas = "id, idCliente, idSalon, fecha"
        self.claves = claveColumnas
        self.reservasTabla = configurarTabla(self, columnas, claveColumnas, base)

        self.setLayout(layout)

    def nuevaReserva(self):
        self.ventana = WindowCarga(self.datos, self.claves, self.tabla)
        defaultWindow(self.ventana)

    def borrarReserva(self):
        filaSeleccionada = self.reservasTabla.selectedItems()
        if filaSeleccionada:
            fila = filaSeleccionada[0].row()
            fId = self.reservasTabla.item(fila,0).text()
            self.reservasTabla.removeRow(fila)
            self.reservasTabla.clearSelection()
            borrado(self.tabla, fId)
        else:
            QMessageBox.critical(self, "Borrar", "Seleccione una fila.   ", QMessageBox.Ok)

class WindowSalones(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = layout = QVBoxLayout()

        botonTabla(self, "Editar", 20, 20, self.editar)

        columnas = ("ID: ", "Salon: ")
        self.datos = columnas
        claveColumnas = "id, salon"
        self.claves = claveColumnas
        base = "salones"
        self.tabla = base
        self.clientesTabla = configurarTabla(self, columnas, claveColumnas, base)

        self.setLayout(layout)

    def editar(self):
        pass

class WindowClientes(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = layout = QVBoxLayout()

        botonTabla(self, "Nuevo", 20, 20, self.nuevaCarga)
        botonTabla(self, "Editar", 180, 20, self.editarDatos)
        botonTabla(self, "Borrar", 340, 20, self.borrarCliente)

        columnas = ("ID: ", "Nombre: ", "Email: ", "Telefono: ", "Ciudad: ")
        self.datos = columnas
        claveColumnas = "id, nombre, email, numero, ciudad"
        self.claves = claveColumnas
        base = "clientes"
        self.tabla = base
        self.clientesTabla = configurarTabla(self, columnas, claveColumnas, base)

        self.setLayout(layout)

    def nuevaCarga(self):
        self.ventana = WindowCarga(self.datos, self.claves, self.tabla)
        defaultWindow(self.ventana)  

    def editarDatos(self):
        filaSeleccionada = self.clientesTabla.selectedItems()
        self.ventana = WindowEditar(filaSeleccionada, self.clientesTabla, self.claves, self.datos)
        defaultWindow(self.ventana)

    def borrarCliente(self):
        filaSeleccionada = self.clientesTabla.selectedItems()
        if filaSeleccionada:
            fila = filaSeleccionada[1].row()
            print(fila)
            fId = self.clientesTabla.item(fila,0).text()
            self.clientesTabla.removeRow(fila)
            self.clientesTabla.clearSelection()
            #borrado(self.tabla, fId)
        else:
            QMessageBox.critical(self, "Borrar", "Seleccione una fila.   ", QMessageBox.Ok)    
        
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent) 
        self.layout = layout = QVBoxLayout()

        self.texto = QLabel("Argentalia")
        self.texto.setFont(QFont("Arial", 35))
        layout.addWidget(self.texto)

        dia = Fecha()
        self.fecha = QLabel(f"Fecha: {dia.fechaActual()}")
        self.fecha.setFont(QFont("Arial", 30))
        layout.addWidget(self.fecha)

        self.botonClientes = QPushButton("Clientes")
        botonMainMenu(self.botonClientes, layout, self.arranqueClientes)
        self.botonSalones = QPushButton("Salones")
        botonMainMenu(self.botonSalones, layout, self.arranqueSalones)
        self.botonReservas = QPushButton("Reservas")
        botonMainMenu(self.botonReservas, layout, self.arranqueReservas)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def arranqueClientes(self):
        self.ventana = WindowClientes()
        defaultWindow(self.ventana)

    def arranqueSalones(self):
        self.ventana = WindowSalones()
        defaultWindow(self.ventana)

    def arranqueReservas(self):
        self.ventana = WindowReservas()
        defaultWindow(self.ventana)

if __name__ == '__main__':
    app = QApplication()
    css = '*{background-color: #36393f; color: white;selection-color: gray;selection-background-color: blue;}'
    app.setStyleSheet(css)
    window = MainWindow()
    window.resize(800,600)
    window.show()
    app.exec()