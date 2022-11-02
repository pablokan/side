from database import Database

choferes = Database("Choferes", "nombre", "dni", "gamaAuto")

def agregarChofer(nombre, dni, gamaAuto):
    return choferes.insert(nombre, dni, gamaAuto)

def eliminarChofer(nombre: str):
    data = choferes.select()
    for i in range(len(data)):
        if data[i][1] == nombre:
            return choferes.delete(data[i][0])

def traerDatosChoferes(info: str):
    data = choferes.select()
    datos = list()
    for i in range(len(data)):
        if info == "nombres":
            datos.append(data[i][1])
        elif info == "gama":
            datos.append(data[i][3])
    return datos

