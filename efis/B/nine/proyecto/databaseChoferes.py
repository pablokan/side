from database import Database

choferes = Database("Choferes", "nombre", "dni", "gamaAuto")

def agregar(nombre, dni, gamaAuto):
    return choferes.insert(nombre, dni, gamaAuto)

def eliminar(nombre: str):
    data = choferes.select()
    for i in range(len(data)):
        if data[i][1] == nombre:
            return choferes.delete(data[i][0])

def traerDatos(info: str):
    data = choferes.select()
    datos = list()
    for i in range(len(data)):
        if info == "nombres":
            datos.append(data[i][1])
        elif info == "gama":
            datos.append(data[i][3])
    return datos

